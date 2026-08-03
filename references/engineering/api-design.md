# API Design

## Core Concept
RESTful/GraphQL/gRPC protocol selection + version management + idempotency + error response design. Create APIs that are consistent, predictable, and easy to consume.

## Applicable Scenarios
✅ **Best for**
- Interface design
- API standardization
- Version compatibility

## Key Steps
1. Choose protocol: RESTful (broad compatibility), GraphQL (flexible queries), gRPC (high performance)
2. Design resource naming (nouns, not verbs for REST)
3. Implement versioning: URL path (/v1/) or header-based
4. Design consistent error responses: status code + error code + message + details
5. Ensure idempotency for write operations (idempotency keys)
6. Document with OpenAPI/Protobuf; provide SDKs

## Source
REST: Roy Fieldting (2000); API design best practices from industry standards.
