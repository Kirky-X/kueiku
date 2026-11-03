# API Design

## Core Concept
RESTful/GraphQL/gRPC protocol selection + version management + idempotency + error response design. Create APIs that are consistent, predictable, and easy to consume.

## Applicable Scenarios
✅ **Best for**
- Interface design
- API standardization
- Version compatibility

⚠️ **When NOT to use**
- The protocol choice is already made by infrastructure reality — gRPC inside a mesh, REST at the edge, GraphQL only because a client cannot express its query another way → the protocol-selection step becomes theater and the useful part is versioning, idempotency, and error shape
- Service boundary questions ("should this be its own service?") → **Domain-Driven Design** / **Microservices Patterns** settle boundaries first; the API inherits them and cannot fix a wrong seam
- Service-to-service contracts where the producer and consumer are both internal and versioned together → a public-style REST contract adds ceremony without a consumer boundary; **Typed Service Contracts** fits internal edges better
- CLI and tool surfaces meant for agents rather than network clients → **Agent DX / CLI Scale** scores the interface an agent actually touches

## Key Steps
1. Choose protocol: RESTful (broad compatibility), GraphQL (flexible queries), gRPC (high performance)
2. Design resource naming (nouns, not verbs for REST)
3. Implement versioning: URL path (/v1/) or header-based
4. Design consistent error responses: status code + error code + message + details
5. Ensure idempotency for write operations (idempotency keys)
6. Document with OpenAPI/Protobuf; provide SDKs

## Output Template

```
API: [name]     Consumers: [service A, partner B, mobile app]     Owner: [team]

Protocol: [REST | GraphQL | gRPC] — why: [client capability, latency budget, ecosystem]

Resources (all under /v1):
  GET    /v1/[resource]        → [200 body shape]
  POST   /v1/[resource]        → [201 body shape]   idempotency: key [header], TTL [24h]
  PATCH  /v1/[resource]/{id}   → [200 body shape]   idempotency: [natural | key]

Versioning: [path /v1 | header] — breaking → [v2], additive → [v1]
Deprecation: [Sunset header date] — old version stays until [date], then removed

Error envelope (same shape on every endpoint):
  { "code": "[MACHINE_CODE]", "message": "[human text]", "details": [...], "trace_id": "[id]" }
  HTTP status: [400] [401] [404] [409] [422] [429] [500] — each mapped to a code

Auth: [scheme + scope model]   Rate limit: [rule]   Pagination: [cursor field]
Contract test suite: [name] — CI gate fails when the schema changes incompatibly
Spec location: [openapi/proto path or url]
```

## Failure Modes
- Versioning decided per client whim, so every consumer negotiates its own scheme → fix one deprecation policy (sunset date plus migration window) and enforce the schema with contract tests, so an incompatible change breaks the build instead of production
- Idempotency keys added to POST only, leaving PATCH and DELETE unsafe to retry → a key helps only if the server persists the outcome and replays the same response; give every state-changing endpoint a key or document which are naturally idempotent
- Error envelopes designed per endpoint, so each client writes its own parser → define one error body and validate it in CI against every endpoint, rejecting anything that drifts
- New version shipped but the old one never retired, so both stay live and both need maintenance → put a removal date in the version itself and check live traffic per version before deleting it
- Spec written by hand and drifting from the implementation, so it is trusted by nobody → generate the spec from the implementation or run its examples as tests; a spec no test consumes is prose

## Evidence Strength
Mixed — REST conventions, resource naming, and error-envelope consistency are among the most widely adopted and best documented interface practices, and versioning and idempotency key mechanisms have solid engineering rationale; the comparative evidence that a particular protocol or versioning scheme yields better outcomes for a given context is weak and largely observational, so protocol choice should follow client constraints rather than a generalized claim.

## Source
REST: Roy Fieldting (2000); API design best practices from industry standards.
