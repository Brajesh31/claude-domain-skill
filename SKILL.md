---
name: railway-domain
description: Add, inspect, validate, and remove Railway service domains using the Railway CLI or an explicitly authorized integration.
---

# Railway Domain Management

## Scope
Manage domain configuration for Railway services. This skill does not manage domain purchases, registrar accounts, unrelated DNS providers, or application routing beyond the service's domain configuration.

## Before acting
Identify the linked project, environment, target service, domain type, and required port. If any target is ambiguous, ask before changing configuration.

## Inspect
Use the installed Railway CLI or an authorized integration to establish the current project, environment, service, and deployment state. Do not guess resource identifiers.

## Add a platform domain
Use the CLI syntax supported by the installed version and target the intended service. Confirm that a deployment exists and capture the returned hostname exactly.

## Add a custom domain
Validate hostname syntax first. Request the custom-domain operation and relay the exact DNS records returned by the platform. Do not invent CNAME, A, or TXT values. DNS propagation and certificate provisioning are separate states.

## Read and remove
Read current configuration before proposing removal. Removing a domain can interrupt traffic. Require explicit confirmation, identify the exact hostname and service, then verify the resulting configuration.

## Safety
- Never expose API tokens or environment secrets.
- Never claim DNS has propagated without checking.
- Do not modify registrar DNS unless separately authorized and supported.
- Do not remove a domain based on an ambiguous request.
- Treat CLI output as authoritative for generated records and resource IDs.

See resources/domain-lifecycle.md and resources/dns-records.md.