# Railway Domain Lifecycle

## Lifecycle
1. Confirm project, environment, and service.
2. Inspect deployment state.
3. Determine generated hostname or custom hostname.
4. Request the domain operation.
5. Capture exact response and DNS instructions.
6. Verify the domain appears in service configuration.
7. Obtain explicit confirmation before removal.
8. Verify the hostname is no longer configured after removal.

## Platform hostname
A platform-provided hostname is attached to a deployed service. Confirm current platform limits and deployment requirements instead of assuming them.

## Custom hostname
The platform may return DNS records that must be created at the authoritative DNS provider. Copy record type, host/name, and value exactly. Do not substitute generic values.

## Operational checks
- Confirm the service listens on the configured port.
- Confirm the application binds to the expected interface.
- Check deployment health after attaching the domain.
- Confirm TLS provisioning separately from DNS record creation.
- Test the public hostname only after DNS and certificate state are ready.