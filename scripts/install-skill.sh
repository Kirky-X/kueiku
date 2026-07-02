#!/usr/bin/env bash
# install-skill.sh — 安装/卸载 skill 到项目级 agent 目录
#
# 子命令:
#   install <skill>     安装 skill 到目标项目的 agent 目录
#   uninstall <skill>   卸载 skill
#   list-skills         列出可安装的 skill
#   list-agents         列出支持的 agent 类型及安装路径
#   status              显示目标项目中已安装的 skill
#   generate-commands <skill>  为 skill 子命令生成 agent commands 文件
#
# 支持两种部署模式（自动识别）：
#   1. 多 skill 父目录模式：脚本在 <root>/scripts/ 下，<root>/<skill-name>/ 有 SKILL.md
#   2. 独立 skill 仓库模式：脚本在 <skill-repo>/scripts/ 下，<skill-repo>/SKILL.md 直接存在
#      此模式下 skill-name 必须等于 <skill-repo> 的 basename，install/list-skills 才能工作

set -euo pipefail

# ---------- 定位项目根（文件副本或软链接调用均支持）----------
SCRIPT_REAL_PATH="$(readlink -f "$0")"
SCRIPT_DIR="$(cd "$(dirname "$SCRIPT_REAL_PATH")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# ---------- 模式识别：独立 skill 仓库 vs 多 skill 父目录 ----------
# 独立 skill 仓库模式：PROJECT_ROOT/SKILL.md 直接存在
# 此模式下 PROJECT_ROOT 本身就是 skill 源目录
is_standalone_skill_repo() {
  [[ -f "$PROJECT_ROOT/SKILL.md" ]]
}

# 解析 skill 源目录路径（stdout）
# 用法: resolve_skill_src <skill-name>
# 多 skill 模式: $PROJECT_ROOT/<skill-name>
# 独立仓库模式: $PROJECT_ROOT（当且仅当 skill-name == basename(PROJECT_ROOT)）
# 失败时返回空字符串（stderr 由调用方打印）
resolve_skill_src() {
  local skill_name="$1"
  if is_standalone_skill_repo; then
    if [[ "$(basename "$PROJECT_ROOT")" == "$skill_name" ]]; then
      printf '%s\n' "$PROJECT_ROOT"
      return 0
    fi
    return 1
  fi
  local candidate="$PROJECT_ROOT/$skill_name"
  if [[ -d "$candidate" && -f "$candidate/SKILL.md" ]]; then
    printf '%s\n' "$candidate"
    return 0
  fi
  return 1
}

# ---------- 颜色输出 ----------
if [[ -t 1 ]]; then
  RED=$'\033[31m'; GREEN=$'\033[32m'; YELLOW=$'\033[33m'; BLUE=$'\033[34m'
  BOLD=$'\033[1m'; RESET=$'\033[0m'
else
  RED=''; GREEN=''; YELLOW=''; BLUE=''; BOLD=''; RESET=''
fi

err()  { printf '%s[ERROR]%s %s\n' "$RED" "$RESET" "$*" >&2; }
warn() { printf '%s[WARN]%s  %s\n' "$YELLOW" "$RESET" "$*" >&2; }
info() { printf '%s[INFO]%s  %s\n' "$BLUE" "$RESET" "$*"; }

# ---------- agent 映射 ----------
# 格式: agent_name|folder|skill_subdir
AGENTS=(
  "claude|.claude|skills"
  "cursor|.cursor|rules"
  "windsurf|.windsurf|rules"
  "trae|.trae|rules"
  "gemini|.gemini|skills"
  "copilot|.github|prompts"
  "opencode|.opencode|skills"
  "roocode|.roo|skills"
  "qoder|.qoder|rules"
)
ALL_AGENT_NAMES=(claude cursor windsurf trae gemini copilot opencode roocode qoder)

# 排除项（相对 skill 源目录的顶层条目）
EXCLUDE_PATTERNS=(.git .venv node_modules __pycache__ temp .gitnexus .claude)

# ---------- 用法 ----------
usage() {
  cat <<'EOF'
Usage: install-skill.sh <command> [options]

Commands:
  install <skill-name> [--target <dir>] [--agent <type>|--all-agents]
      安装 skill 到目标项目的 agent 目录（默认 --target .  默认 --agent claude）
  uninstall <skill-name> [--target <dir>] [--agent <type>|--all-agents]
      卸载 skill
  list-skills
      列出可安装的 skill（扫描项目根下含 SKILL.md 的目录）
  list-agents
      列出支持的 agent 类型及安装路径
  status [--target <dir>]
      显示目标项目中已安装的 skill
  generate-commands <skill-name> [--target <dir>] [--agent <type>|--all-agents] [--commands <cmd1,cmd2,...>]
      为 skill 的每个子命令生成 agent commands 文件（<target>/<folder>/commands/<skill>-<sub>.md）
      子命令来源：--commands 显式指定 > SKILL.md argument-hint > SKILL.md 路由表扫描

Options:
  --target <dir>   目标项目目录（默认当前目录 .）
  --agent <type>   指定单个 agent（默认 claude）
  --all-agents     对所有支持的 agent 操作
  --commands <list> 逗号分隔的子命令列表（仅 generate-commands 使用）
  -h, --help       显示此帮助

Agents: claude cursor windsurf trae gemini copilot opencode roocode qoder
EOF
}

# ---------- 解析 install/uninstall 公共选项 ----------
# 全局: TARGET_DIR / AGENT_FLAG
TARGET_DIR="."
AGENT_FLAG=""
parse_target_agent() {
  local args=("$@")
  local i=0
  while [[ $i -lt ${#args[@]} ]]; do
    case "${args[$i]}" in
      --target)
        ((i++)) || true
        [[ $i -lt ${#args[@]} ]] || { err "--target 需要参数"; exit 1; }
        TARGET_DIR="${args[$i]}"
        ;;
      --agent)
        ((i++)) || true
        [[ $i -lt ${#args[@]} ]] || { err "--agent 需要参数"; exit 1; }
        AGENT_FLAG="${args[$i]}"
        ;;
      --all-agents)
        AGENT_FLAG="all"
        ;;
      -h|--help)
        usage; exit 0
        ;;
      *)
        err "未知参数: ${args[$i]}"; usage; exit 1
        ;;
    esac
    ((i++)) || true
  done
}

# 解析 AGENT_FLAG 为 agent 名列表（stdout）
resolve_agents() {
  local flag="${AGENT_FLAG:-claude}"
  if [[ "$flag" == "all" ]]; then
    printf '%s\n' "${ALL_AGENT_NAMES[@]}"
    return
  fi
  local a found=""
  for a in "${ALL_AGENT_NAMES[@]}"; do
    [[ "$a" == "$flag" ]] && { found=1; break; }
  done
  if [[ -z "$found" ]]; then
    err "不支持的 agent 类型: $flag"
    info "支持的 agent: ${ALL_AGENT_NAMES[*]}"
    exit 1
  fi
  printf '%s\n' "$flag"
}

# agent_name -> 输出 "folder|subdir"
agent_config() {
  local name="$1" line
  for line in "${AGENTS[@]}"; do
    if [[ "$line" == "$name|"* ]]; then
      local rest="${line#*|}"   # folder|subdir
      printf '%s\n' "$rest"
      return 0
    fi
  done
  return 1
}

# ---------- 子命令: install ----------
cmd_install() {
  [[ $# -ge 1 ]] || { err "install 需要 <skill-name>"; usage; exit 1; }
  local skill_name="$1"
  shift
  parse_target_agent "$@"

  local src
  src="$(resolve_skill_src "$skill_name")" || {
    err "skill 源目录不存在: $PROJECT_ROOT/$skill_name（独立仓库模式需 skill-name == $(basename "$PROJECT_ROOT")）";
    exit 1;
  }
  [[ -d "$src" ]]      || { err "skill 源目录不存在: $src"; exit 1; }
  [[ -f "$src/SKILL.md" ]] || { err "skill 源目录缺少 SKILL.md: $src/SKILL.md"; exit 1; }

  [[ -d "$TARGET_DIR" ]] || mkdir -p "$TARGET_DIR"
  TARGET_DIR="$(cd "$TARGET_DIR" && pwd)"

  local agents failed=0
  agents="$(resolve_agents)"

  printf '%s%-10s %-58s %-8s%s\n' "$BOLD" "AGENT" "PATH" "STATUS" "$RESET"
  printf '%.0s-' {1..80}; printf '\n'

  local agent
  while IFS= read -r agent; do
    local cfg folder subdir dest
    cfg="$(agent_config "$agent")" || { err "内部错误: agent_config $agent"; exit 1; }
    folder="${cfg%%|*}"
    subdir="${cfg##*|}"
    dest="$TARGET_DIR/$folder/$subdir/$skill_name"

    # 清理后重建，避免残留旧文件
    rm -rf "$dest"
    mkdir -p "$dest"

    # 复制源目录顶层条目，跳过排除项（避免复制 .venv / .git 等大目录）
    # 纯 bash 实现：dotglob 让 * 匹配隐藏文件，遍历时按名跳过 EXCLUDE_PATTERNS
    local item ename p excluded cp_failed=0
    local _dg=0 _ng=0
    shopt -q dotglob  && _dg=1
    shopt -q nullglob && _ng=1
    shopt -s dotglob nullglob
    for item in "$src"/*; do
      [[ -e "$item" ]] || continue
      ename="$(basename "$item")"
      excluded=0
      for p in "${EXCLUDE_PATTERNS[@]}"; do
        [[ "$ename" == "$p" ]] && { excluded=1; break; }
      done
      [[ $excluded -eq 1 ]] && continue
      if ! cp -r "$item" "$dest/" 2>/dev/null; then
        cp_failed=1
        break
      fi
    done
    [[ $_dg -eq 0 ]] && shopt -u dotglob
    [[ $_ng -eq 0 ]] && shopt -u nullglob

    if [[ $cp_failed -ne 0 ]]; then
      err "复制失败: $src -> $dest"
      failed=1
      printf '%-10s %-58s %s%s%s\n' "$agent" "$dest" "$RED" "FAILED" "$RESET"
      continue
    fi
    # specmark/changes 为运行时产物（specmark skill 本身保留）
    rm -rf "$dest/specmark/changes" 2>/dev/null || true

    printf '%-10s %-58s %s%s%s\n' "$agent" "$dest" "$GREEN" "OK" "$RESET"
  done <<< "$agents"

  [[ $failed -ne 0 ]] && exit 1
  return 0
}

# ---------- 子命令: uninstall ----------
cmd_uninstall() {
  [[ $# -ge 1 ]] || { err "uninstall 需要 <skill-name>"; usage; exit 1; }
  local skill_name="$1"
  shift
  parse_target_agent "$@"

  [[ -d "$TARGET_DIR" ]] || { err "目标目录不存在: $TARGET_DIR"; exit 1; }
  TARGET_DIR="$(cd "$TARGET_DIR" && pwd)"

  local agents
  agents="$(resolve_agents)"

  printf '%s%-10s %-58s %-8s%s\n' "$BOLD" "AGENT" "PATH" "STATUS" "$RESET"
  printf '%.0s-' {1..80}; printf '\n'

  local agent
  while IFS= read -r agent; do
    local cfg folder subdir dest
    cfg="$(agent_config "$agent")" || continue
    folder="${cfg%%|*}"
    subdir="${cfg##*|}"
    dest="$TARGET_DIR/$folder/$subdir/$skill_name"

    if [[ -d "$dest" ]]; then
      rm -rf "$dest"
      printf '%-10s %-58s %s%s%s\n' "$agent" "$dest" "$GREEN" "REMOVED" "$RESET"
    else
      printf '%-10s %-58s %s%s%s\n' "$agent" "$dest" "$YELLOW" "ABSENT" "$RESET"
    fi
  done <<< "$agents"
}

# ---------- 子命令: list-skills ----------
cmd_list_skills() {
  printf '%s%-12s %s%s\n' "$BOLD" "NAME" "DESCRIPTION" "$RESET"
  printf '%.0s-' {1..80}; printf '\n'
  local found=0 d name dir desc

  # 独立 skill 仓库模式：PROJECT_ROOT 本身就是 skill
  if is_standalone_skill_repo; then
    name="$(basename "$PROJECT_ROOT")"
    desc="$(grep -m1 '^description:' "$PROJECT_ROOT/SKILL.md" 2>/dev/null || true)"
    desc="${desc#description:}"
    desc="${desc# }"
    desc="${desc#\"}"; desc="${desc%\"}"
    desc="${desc#\'}"; desc="${desc%\'}"
    if [[ ${#desc} -gt 80 ]]; then
      desc="${desc:0:77}..."
    fi
    printf '%-12s %s\n' "$name" "$desc"
    return
  fi

  # 多 skill 父目录模式：扫描 PROJECT_ROOT/*/ 下的 skill
  for d in "$PROJECT_ROOT"/*/; do
    [[ -d "$d" ]] || continue
    dir="${d%/}"
    name="$(basename "$dir")"
    [[ "$name" == "temp" ]] && continue
    [[ -f "$dir/SKILL.md" ]] || continue
    desc="$(grep -m1 '^description:' "$dir/SKILL.md" 2>/dev/null || true)"
    desc="${desc#description:}"
    desc="${desc# }"               # 去前导空格
    # 去首尾引号
    desc="${desc#\"}"; desc="${desc%\"}"
    desc="${desc#\'}"; desc="${desc%\'}"
    # 截断到 80 字符
    if [[ ${#desc} -gt 80 ]]; then
      desc="${desc:0:77}..."
    fi
    printf '%-12s %s\n' "$name" "$desc"
    found=1
  done
  if [[ $found -eq 0 ]]; then
    warn "未在 $PROJECT_ROOT 下找到任何 skill"
  fi
}

# ---------- 子命令: list-agents ----------
cmd_list_agents() {
  printf '%s%-10s %-12s %-10s %s%s\n' "$BOLD" "AGENT" "FOLDER" "SUBDIR" "FULL PATH" "$RESET"
  printf '%.0s-' {1..80}; printf '\n'
  local line name folder subdir
  for line in "${AGENTS[@]}"; do
    name="${line%%|*}"
    folder="${line#*|}"; folder="${folder%%|*}"
    subdir="${line##*|}"
    printf '%-10s %-12s %-10s %s\n' "$name" "$folder" "$subdir" "$folder/$subdir/<skill>/"
  done
}

# ---------- 子命令: status ----------
cmd_status() {
  TARGET_DIR="."
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --target)
        shift
        [[ $# -gt 0 ]] || { err "--target 需要参数"; exit 1; }
        TARGET_DIR="$1"
        ;;
      -h|--help) usage; exit 0 ;;
      *) err "未知参数: $1"; usage; exit 1 ;;
    esac
    shift
  done

  [[ -d "$TARGET_DIR" ]] || { err "目标目录不存在: $TARGET_DIR"; exit 1; }
  TARGET_DIR="$(cd "$TARGET_DIR" && pwd)"

  printf '目标: %s\n' "$TARGET_DIR"
  printf '%s%-10s %-14s %s%s\n' "$BOLD" "AGENT" "SKILL" "PATH" "$RESET"
  printf '%.0s-' {1..80}; printf '\n'
  local any=0 line name folder subdir base sd sname
  for line in "${AGENTS[@]}"; do
    name="${line%%|*}"
    folder="${line#*|}"; folder="${folder%%|*}"
    subdir="${line##*|}"
    base="$TARGET_DIR/$folder/$subdir"
    [[ -d "$base" ]] || continue
    for sd in "$base"/*/; do
      [[ -d "$sd" ]] || continue
      [[ -f "${sd}SKILL.md" ]] || continue
      sname="$(basename "$sd")"
      printf '%-10s %-14s %s\n' "$name" "$sname" "${sd%/}"
      any=1
    done
  done
  if [[ $any -eq 0 ]]; then
    warn "未在 $TARGET_DIR 下发现已安装的 skill"
  fi
}

# ---------- 子命令: generate-commands ----------
# 从 skill 的 SKILL.md 提取子命令列表（stdout，每行一个）
# 用法: extract_subcommands <skillmd>
# 策略 1: frontmatter `argument-hint: "[cmd1|cmd2|...]"`
# 策略 2: markdown 表格行 | `cmd` | 描述 |
extract_subcommands() {
  local skillmd="$1"
  # 策略 1: argument-hint frontmatter
  local hint
  hint="$(grep -m1 '^argument-hint:' "$skillmd" 2>/dev/null || true)"
  if [[ -n "$hint" && "$hint" =~ \[([^\]]+)\] ]]; then
    local inner="${BASH_REMATCH[1]}"
    local -a cmds=() cmd
    IFS='|' read -ra cmds <<< "$inner"
    for cmd in "${cmds[@]}"; do
      cmd="${cmd// /}"
      [[ -n "$cmd" ]] && printf '%s\n' "$cmd"
    done
    return 0
  fi
  # 策略 2: markdown 表格行 | `cmd` | ...
  local line
  while IFS= read -r line; do
    if [[ "$line" =~ ^\|[[:space:]]*\`([a-z][a-z0-9-]*)\`[[:space:]]*\| ]]; then
      printf '%s\n' "${BASH_REMATCH[1]}"
    fi
  done < "$skillmd"
}

# 从 SKILL.md 提取子命令描述（stdout）
# 用法: extract_subcommand_desc <skillmd> <subcommand>
# 策略: 表格行 | `sub` | 描述 | ... → 取第 3 列；兜底 "执行 <sub> 任务"
extract_subcommand_desc() {
  local skillmd="$1" sub="$2"
  local line desc=""
  line="$(grep -E "^\|[[:space:]]*\`$sub\`[[:space:]]*\|" "$skillmd" 2>/dev/null | head -n1 || true)"
  if [[ -n "$line" ]]; then
    desc="$(printf '%s' "$line" | awk -F'|' '{gsub(/^[ \t]+|[ \t]+$/, "", $3); print $3}')"
  fi
  if [[ -z "$desc" ]]; then
    desc="执行 $sub 任务"
  fi
  printf '%s\n' "$desc"
}

cmd_generate_commands() {
  [[ $# -ge 1 ]] || { err "generate-commands 需要 <skill-name>"; usage; exit 1; }
  local skill_name="$1"
  shift

  local commands_arg=""
  TARGET_DIR="."
  AGENT_FLAG=""

  while [[ $# -gt 0 ]]; do
    case "$1" in
      --target)
        shift
        [[ $# -gt 0 ]] || { err "--target 需要参数"; exit 1; }
        TARGET_DIR="$1"
        ;;
      --agent)
        shift
        [[ $# -gt 0 ]] || { err "--agent 需要参数"; exit 1; }
        AGENT_FLAG="$1"
        ;;
      --all-agents)
        AGENT_FLAG="all"
        ;;
      --commands)
        shift
        [[ $# -gt 0 ]] || { err "--commands 需要参数"; exit 1; }
        commands_arg="$1"
        ;;
      -h|--help) usage; exit 0 ;;
      *) err "未知参数: $1"; usage; exit 1 ;;
    esac
    shift
  done

  local src
  src="$(resolve_skill_src "$skill_name")" || {
    err "skill 源目录不存在: $PROJECT_ROOT/$skill_name（独立仓库模式需 skill-name == $(basename "$PROJECT_ROOT")）";
    exit 1;
  }
  local skillmd="$src/SKILL.md"
  [[ -f "$skillmd" ]] || { err "skill 源目录缺少 SKILL.md: $skillmd"; exit 1; }

  [[ -d "$TARGET_DIR" ]] || mkdir -p "$TARGET_DIR"
  TARGET_DIR="$(cd "$TARGET_DIR" && pwd)"

  # 解析子命令列表
  local subcommands=() s
  if [[ -n "$commands_arg" ]]; then
    local -a cmds=()
    IFS=',' read -ra cmds <<< "$commands_arg"
    for s in "${cmds[@]}"; do
      s="${s// /}"
      [[ -n "$s" ]] && subcommands+=("$s")
    done
  else
    local raw
    raw="$(extract_subcommands "$skillmd")"
    if [[ -n "$raw" ]]; then
      while IFS= read -r s; do
        [[ -n "$s" ]] && subcommands+=("$s")
      done <<< "$raw"
    fi
  fi

  if [[ ${#subcommands[@]} -eq 0 ]]; then
    err "未能从 SKILL.md 提取子命令，且未指定 --commands"
    info "用法: generate-commands <skill> --commands cmd1,cmd2,... [--target <dir>] [--agent <type>|--all-agents]"
    exit 1
  fi

  # 去重，保留顺序
  local seen="" unique_subs=()
  for s in "${subcommands[@]}"; do
    if [[ " $seen " != *" $s "* ]]; then
      unique_subs+=("$s")
      seen="$seen $s"
    fi
  done

  local agents
  agents="$(resolve_agents)"

  printf '%s%-10s %-58s %-8s%s\n' "$BOLD" "AGENT" "COMMANDS DIR" "STATUS" "$RESET"
  printf '%.0s-' {1..80}; printf '\n'

  local agent failed=0
  while IFS= read -r agent; do
    local cfg folder subdir cmddir
    cfg="$(agent_config "$agent")" || { err "内部错误: agent_config $agent"; exit 1; }
    folder="${cfg%%|*}"
    subdir="${cfg##*|}"
    cmddir="$TARGET_DIR/$folder/commands"

    mkdir -p "$cmddir"

    local sub desc file created=0
    for sub in "${unique_subs[@]}"; do
      desc="$(extract_subcommand_desc "$skillmd" "$sub")"
      file="$cmddir/$skill_name-$sub.md"
      cat > "$file" <<EOF
---
description: $desc
---

使用 $skill_name skill 的 $sub 子命令进行以下任务：$desc。
EOF
      created=$((created+1))
    done

    printf '%-10s %-58s %s%s%s (%d cmds)\n' "$agent" "$cmddir" "$GREEN" "OK" "$RESET" "$created"
  done <<< "$agents"

  [[ $failed -ne 0 ]] && exit 1
  return 0
}

# ---------- 主分发 ----------
main() {
  [[ $# -lt 1 ]] && { usage; exit 1; }
  local cmd="$1"
  shift
  case "$cmd" in
    install)           cmd_install "$@" ;;
    uninstall)         cmd_uninstall "$@" ;;
    list-skills)       cmd_list_skills ;;
    list-agents)       cmd_list_agents ;;
    status)            cmd_status "$@" ;;
    generate-commands) cmd_generate_commands "$@" ;;
    -h|--help)         usage; exit 0 ;;
    *) err "未知命令: $cmd"; usage; exit 1 ;;
  esac
}

main "$@"
