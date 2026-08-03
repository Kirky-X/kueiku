#!/usr/bin/env bash
# install-skill.sh — Install/Update/Uninstall skill to project-level agent directory
#
# subcommands:
#   install <skill>     Install skill to target project's agent directory
#   update [skill]      Pull latest version from git and reinstall (all if no skill specified)
#   uninstall <skill>   Uninstall skill
#   list-skills         List available skills
#   list-agents         List supported agent types and install paths
#   status              Show installed skills in target project
#   generate-commands <skill>  Generate agent command files for skill subcommands
#
# Supports two deployment modes (auto-detected):
#   1. Multi-skill parent directory: Script in <root>/scripts/, <root>/<skill-name>/ has SKILL.md
#   2. Standalone skill repo: Script in <skill-repo>/scripts/, <skill-repo>/SKILL.md exists directly
#      In this mode skill-name must equal <skill-repo> basename for install/list-skills to work

set -euo pipefail

# ---------- Locate project root (supports file copy or symlink invocation) ----------
SCRIPT_REAL_PATH="$(readlink -f "$0")"
SCRIPT_DIR="$(cd "$(dirname "$SCRIPT_REAL_PATH")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# ---------- Mode detection: standalone skill repo vs multi-skill parent directory ----------
# Standalone skill repo mode: PROJECT_ROOT/SKILL.md exists directly
# In this mode PROJECT_ROOT itself is the skill source directory
is_standalone_skill_repo() {
  [[ -f "$PROJECT_ROOT/SKILL.md" ]]
}

# Parse skill source directory path (stdout)
# Usage: resolve_skill_src <skill-name>
# Multi-skill mode: $PROJECT_ROOT/<skill-name>
# Standalone repo mode: $PROJECT_ROOT (only when skill-name == basename(PROJECT_ROOT))
# Returns empty string on failure (stderr printed by caller)
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

# ---------- Color output ----------
if [[ -t 1 ]]; then
  RED=$'\033[31m'; GREEN=$'\033[32m'; YELLOW=$'\033[33m'; BLUE=$'\033[34m'
  BOLD=$'\033[1m'; RESET=$'\033[0m'
else
  RED=''; GREEN=''; YELLOW=''; BLUE=''; BOLD=''; RESET=''
fi

err()  { printf '%s[ERROR]%s %s\n' "$RED" "$RESET" "$*" >&2; }
warn() { printf '%s[WARN]%s  %s\n' "$YELLOW" "$RESET" "$*" >&2; }
info() { printf '%s[INFO]%s  %s\n' "$BLUE" "$RESET" "$*"; }

# ---------- agent mapping ----------
# Format: agent_name|folder|skill_subdir
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

# Exclusion patterns (top-level entries relative to skill source directory)
EXCLUDE_PATTERNS=(.git .venv node_modules __pycache__ temp .codenexus .claude)

# ---------- Usage ----------
usage() {
  cat <<'EOF'
Usage: install-skill.sh <command> [options]

Commands:
  install <skill-name> [--target <dir>] [--agent <type>|--all-agents]
      Install skill to target project's agent directory (default --target . default --agent claude)
  update [skill-name] [--target <dir>] [--agent <type>|--all-agents]
      Pull latest version from git and reinstall. Updates all skills if no skill-name specified
  uninstall <skill-name> [--target <dir>] [--agent <type>|--all-agents]
      Uninstall skill
  list-skills
      List available skills (scans project root for directories with SKILL.md)
  list-agents
      List supported agent types and install paths
  status [--target <dir>]
      Show installed skills in target project
  generate-commands <skill-name> [--target <dir>] [--agent <type>|--all-agents] [--commands <cmd1,cmd2,...>]
      Generate agent command files for each skill subcommand (<target>/<folder>/commands/<skill>-<sub>.md)
      Subcommand source: --commands explicit > SKILL.md argument-hint > SKILL.md routing table scan

Options:
  --target <dir>   Target project directory (default current directory .)
  --agent <type>   Specify single agent (default claude)
  --all-agents     Operate on all supported agents
  --commands <list> Comma-separated subcommand list (only used by generate-commands)
  -h, --help       Show this help

Agents: claude cursor windsurf trae gemini copilot opencode roocode qoder
EOF
}

# ---------- Parse install/uninstall common options ----------
# Global: TARGET_DIR / AGENT_FLAG
TARGET_DIR="."
AGENT_FLAG=""
parse_target_agent() {
  local args=("$@")
  local i=0
  while [[ $i -lt ${#args[@]} ]]; do
    case "${args[$i]}" in
      --target)
        ((i++)) || true
        [[ $i -lt ${#args[@]} ]] || { err "--target requires argument"; exit 1; }
        TARGET_DIR="${args[$i]}"
        ;;
      --agent)
        ((i++)) || true
        [[ $i -lt ${#args[@]} ]] || { err "--agent requires argument"; exit 1; }
        AGENT_FLAG="${args[$i]}"
        ;;
      --all-agents)
        AGENT_FLAG="all"
        ;;
      -h|--help)
        usage; exit 0
        ;;
      *)
        err "Unknown argument: ${args[$i]}"; usage; exit 1
        ;;
    esac
    ((i++)) || true
  done
}

# Parse AGENT_FLAG to agent name list (stdout)
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
    err "Unsupported agent type: $flag"
    info "Supported agents: ${ALL_AGENT_NAMES[*]}"
    exit 1
  fi
  printf '%s\n' "$flag"
}

# agent_name -> Output "folder|subdir"
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

# ---------- subcommand: install ----------
cmd_install() {
  [[ $# -ge 1 ]] || { err "install Requires <skill-name>"; usage; exit 1; }
  local skill_name="$1"
  shift
  parse_target_agent "$@"

  local src
  src="$(resolve_skill_src "$skill_name")" || {
    err "Skill source directory not found: $PROJECT_ROOT/$skill_name (standalone repo mode requires skill-name == $(basename "$PROJECT_ROOT"))";
    exit 1;
  }
  [[ -d "$src" ]]      || { err "Skill source directory not found: $src"; exit 1; }
  [[ -f "$src/SKILL.md" ]] || { err "Skill source directory missing SKILL.md: $src/SKILL.md"; exit 1; }

  [[ -d "$TARGET_DIR" ]] || mkdir -p "$TARGET_DIR"
  TARGET_DIR="$(cd "$TARGET_DIR" && pwd)"

  local agents failed=0
  agents="$(resolve_agents)"

  printf '%s%-10s %-58s %-8s%s\n' "$BOLD" "AGENT" "PATH" "STATUS" "$RESET"
  printf '%.0s-' {1..80}; printf '\n'

  local agent
  while IFS= read -r agent; do
    local cfg folder subdir dest
    cfg="$(agent_config "$agent")" || { err "Internal error: agent_config $agent"; exit 1; }
    folder="${cfg%%|*}"
    subdir="${cfg##*|}"
    dest="$TARGET_DIR/$folder/$subdir/$skill_name"

    # Cleanup and rebuild to avoid stale files
    rm -rf "$dest"
    mkdir -p "$dest"

    # Copy source directory top-level entries, skip exclusions (avoid copying .venv / .git etc.)
    # Pure bash implementation: dotglob makes * match hidden files, skip EXCLUDE_PATTERNS by name during iteration
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
      err "CopyFailure: $src -> $dest"
      failed=1
      printf '%-10s %-58s %s%s%s\n' "$agent" "$dest" "$RED" "FAILED" "$RESET"
      continue
    fi
    # specmark/changes are runtime artifacts (specmark skill itself is preserved)
    rm -rf "$dest/specmark/changes" 2>/dev/null || true

    printf '%-10s %-58s %s%s%s\n' "$agent" "$dest" "$GREEN" "OK" "$RESET"
  done <<< "$agents"

  [[ $failed -ne 0 ]] && exit 1
  return 0
}

# ---------- subcommand: update ----------
cmd_update() {
  local skill_name=""
  TARGET_DIR="."
  AGENT_FLAG=""

  # Parse arguments: first non-flag argument is skill-name (optional)
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --target)
        shift
        [[ $# -gt 0 ]] || { err "--target requires argument"; exit 1; }
        TARGET_DIR="$1"
        ;;
      --agent)
        shift
        [[ $# -gt 0 ]] || { err "--agent requires argument"; exit 1; }
        AGENT_FLAG="$1"
        ;;
      --all-agents)
        AGENT_FLAG="all"
        ;;
      -h|--help)
        usage; exit 0
        ;;
      -*)
        err "Unknown argument: $1"; usage; exit 1
        ;;
      *)
        [[ -z "$skill_name" ]] && skill_name="$1" || { err "Extra argument: $1"; usage; exit 1; }
        ;;
    esac
    shift
  done

  # Step 1: git pull
  info "Pulling latest version..."
  if [[ -d "$PROJECT_ROOT/.git" ]]; then
    if ! git -C "$PROJECT_ROOT" pull --ff-only 2>/dev/null; then
      warn "git pull failed, trying git fetch + reset"
      git -C "$PROJECT_ROOT" fetch origin 2>/dev/null || true
      local current_branch
      current_branch="$(git -C "$PROJECT_ROOT" branch --show-current 2>/dev/null || echo "main")"
      git -C "$PROJECT_ROOT" reset --hard "origin/$current_branch" 2>/dev/null || {
        err "Cannot pull latest version, please git pull manually"
        exit 1
      }
    fi
    info "Latest version pulled"
  else
    warn "Current directory is not a git repo, skipping pull, proceeding with reinstall"
  fi

  # Step 2: Collect skills to update
  local skills=()
  if [[ -n "$skill_name" ]]; then
    skills=("$skill_name")
  else
    # Standalone repo mode: only itself
    if is_standalone_skill_repo; then
      skills=("*")
    else
      # Multi-skill mode: scan all skills
      local d
      for d in "$PROJECT_ROOT"/*/; do
        [[ -d "$d" ]] || continue
        local name
        name="$(basename "$d")"
        [[ "$name" == "temp" ]] && continue
        [[ -f "$d/SKILL.md" ]] || continue
        skills+=("$name")
      done
    fi
  fi

  if [[ ${#skills[@]} -eq 0 ]]; then
    warn "No updatable skills found"
    return 0
  fi

  # Step 3: Update each skill
  printf '%s%-12s %-10s%s\n' "$BOLD" "SKILL" "STATUS" "$RESET"
  printf '%.0s-' {1..40}; printf '\n'

  local s failed=0
  for s in "${skills[@]}"; do
    if [[ "$s" == "*" ]]; then
      # Standalone repo mode: skill name = repo basename
      s="$(basename "$PROJECT_ROOT")"
    fi
    if cmd_install "$s" --target "$TARGET_DIR" --agent "${AGENT_FLAG:-claude}" >/dev/null 2>&1; then
      printf '%-12s %s%s%s\n' "$s" "$GREEN" "UPDATED" "$RESET"
    else
      printf '%-12s %s%s%s\n' "$s" "$RED" "FAILED" "$RESET"
      failed=1
    fi
  done

  [[ $failed -ne 0 ]] && exit 1
  return 0
}

# ---------- subcommand: uninstall ----------
cmd_uninstall() {
  [[ $# -ge 1 ]] || { err "uninstall Requires <skill-name>"; usage; exit 1; }
  local skill_name="$1"
  shift
  parse_target_agent "$@"

  [[ -d "$TARGET_DIR" ]] || { err "Target directory does not exist: $TARGET_DIR"; exit 1; }
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

# ---------- subcommand: list-skills ----------
cmd_list_skills() {
  printf '%s%-12s %s%s\n' "$BOLD" "NAME" "DESCRIPTION" "$RESET"
  printf '%.0s-' {1..80}; printf '\n'
  local found=0 d name dir desc

  # Standalone skill repo mode: PROJECT_ROOT itself is the skill
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

  # Multi-skill parent directory mode: scan PROJECT_ROOT/*/ for skills
  for d in "$PROJECT_ROOT"/*/; do
    [[ -d "$d" ]] || continue
    dir="${d%/}"
    name="$(basename "$dir")"
    [[ "$name" == "temp" ]] && continue
    [[ -f "$dir/SKILL.md" ]] || continue
    desc="$(grep -m1 '^description:' "$dir/SKILL.md" 2>/dev/null || true)"
    desc="${desc#description:}"
    desc="${desc# }"               # Remove leading whitespace
    # Remove surrounding quotes
    desc="${desc#\"}"; desc="${desc%\"}"
    desc="${desc#\'}"; desc="${desc%\'}"
    # Truncate to 80 characters
    if [[ ${#desc} -gt 80 ]]; then
      desc="${desc:0:77}..."
    fi
    printf '%-12s %s\n' "$name" "$desc"
    found=1
  done
  if [[ $found -eq 0 ]]; then
    warn "No skills found in $PROJECT_ROOT"
  fi
}

# ---------- subcommand: list-agents ----------
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

# ---------- subcommand: status ----------
cmd_status() {
  TARGET_DIR="."
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --target)
        shift
        [[ $# -gt 0 ]] || { err "--target requires argument"; exit 1; }
        TARGET_DIR="$1"
        ;;
      -h|--help) usage; exit 0 ;;
      *) err "Unknown argument: $1"; usage; exit 1 ;;
    esac
    shift
  done

  [[ -d "$TARGET_DIR" ]] || { err "Target directory does not exist: $TARGET_DIR"; exit 1; }
  TARGET_DIR="$(cd "$TARGET_DIR" && pwd)"

  printf 'Target: %s\n' "$TARGET_DIR"
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
    warn "No installed skills found in $TARGET_DIR"
  fi
}

# ---------- subcommand: generate-commands ----------
# From skill's SKILL.md extract subcommand list (stdout, one per line)
# Usage: extract_subcommands <skillmd>
# Strategy 1: frontmatter `argument-hint: "[cmd1|cmd2|...]"`
# Strategy 2: markdown table row | `cmd` | description |
extract_subcommands() {
  local skillmd="$1"
  # Strategy 1: argument-hint frontmatter
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
  # Strategy 2: markdown table row | `cmd` | ...
  local line
  while IFS= read -r line; do
    if [[ "$line" =~ ^\|[[:space:]]*\`([a-z][a-z0-9-]*)\`[[:space:]]*\| ]]; then
      printf '%s\n' "${BASH_REMATCH[1]}"
    fi
  done < "$skillmd"
}

# From SKILL.md extract subcommand description (stdout)
# Usage: extract_subcommand_desc <skillmd> <subcommand>
# Strategy: table row | `sub` | description | ... → take 3rd column; fallback "Execute <sub> task"
extract_subcommand_desc() {
  local skillmd="$1" sub="$2"
  local line desc=""
  line="$(grep -E "^\|[[:space:]]*\`$sub\`[[:space:]]*\|" "$skillmd" 2>/dev/null | head -n1 || true)"
  if [[ -n "$line" ]]; then
    desc="$(printf '%s' "$line" | awk -F'|' '{gsub(/^[ \t]+|[ \t]+$/, "", $3); print $3}')"
  fi
  if [[ -z "$desc" ]]; then
    desc="Execute $sub task"
  fi
  printf '%s\n' "$desc"
}

cmd_generate_commands() {
  [[ $# -ge 1 ]] || { err "generate-commands Requires <skill-name>"; usage; exit 1; }
  local skill_name="$1"
  shift

  local commands_arg=""
  TARGET_DIR="."
  AGENT_FLAG=""

  while [[ $# -gt 0 ]]; do
    case "$1" in
      --target)
        shift
        [[ $# -gt 0 ]] || { err "--target requires argument"; exit 1; }
        TARGET_DIR="$1"
        ;;
      --agent)
        shift
        [[ $# -gt 0 ]] || { err "--agent requires argument"; exit 1; }
        AGENT_FLAG="$1"
        ;;
      --all-agents)
        AGENT_FLAG="all"
        ;;
      --commands)
        shift
        [[ $# -gt 0 ]] || { err "--commands requires argument"; exit 1; }
        commands_arg="$1"
        ;;
      -h|--help) usage; exit 0 ;;
      *) err "Unknown argument: $1"; usage; exit 1 ;;
    esac
    shift
  done

  local src
  src="$(resolve_skill_src "$skill_name")" || {
    err "Skill source directory not found: $PROJECT_ROOT/$skill_name (standalone repo mode requires skill-name == $(basename "$PROJECT_ROOT"))";
    exit 1;
  }
  local skillmd="$src/SKILL.md"
  [[ -f "$skillmd" ]] || { err "Skill source directory missing SKILL.md: $skillmd"; exit 1; }

  [[ -d "$TARGET_DIR" ]] || mkdir -p "$TARGET_DIR"
  TARGET_DIR="$(cd "$TARGET_DIR" && pwd)"

  # Parse subcommand list
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
    err "Could not extract subcommands from SKILL.md, and --commands not specified"
    info "Usage: generate-commands <skill> --commands cmd1,cmd2,... [--target <dir>] [--agent <type>|--all-agents]"
    exit 1
  fi

  # Deduplicate, preserve order
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
    cfg="$(agent_config "$agent")" || { err "Internal error: agent_config $agent"; exit 1; }
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

Use $skill_name skill's $sub subcommand for the following task: $desc.
EOF
      created=$((created+1))
    done

    printf '%-10s %-58s %s%s%s (%d cmds)\n' "$agent" "$cmddir" "$GREEN" "OK" "$RESET" "$created"
  done <<< "$agents"

  [[ $failed -ne 0 ]] && exit 1
  return 0
}

# ---------- Main dispatch ----------
main() {
  [[ $# -lt 1 ]] && { usage; exit 1; }
  local cmd="$1"
  shift
  case "$cmd" in
    install)           cmd_install "$@" ;;
    update)            cmd_update "$@" ;;
    uninstall)         cmd_uninstall "$@" ;;
    list-skills)       cmd_list_skills ;;
    list-agents)       cmd_list_agents ;;
    status)            cmd_status "$@" ;;
    generate-commands) cmd_generate_commands "$@" ;;
    -h|--help)         usage; exit 0 ;;
    *) err "Unknown command: $cmd"; usage; exit 1 ;;
  esac
}

main "$@"
