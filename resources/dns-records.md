# DNS Records for Service Domains

## Common record types
- A: maps a hostname to an IPv4 address.
- AAAA: maps a hostname to an IPv6 address.
- CNAME: aliases one hostname to another hostname.
- TXT: stores verification or policy text.

## Record handling
When the platform returns required DNS records, preserve:
- Type.
- Host or record name.
- Target or value.
- TTL, if specified.
- Verification status or instructions.

DNS providers represent zone apexes and subdomains differently. Explain how to enter the returned host value in the provider's interface, but do not change the target.

## Verification
Use authoritative DNS lookup tools to confirm records are visible. DNS visibility does not prove that the application is healthy or that TLS has been provisioned.

Never invent a record target or ask the user to publish secrets in a public DNS record.