# Security API

The Security API replaces parts of Logi Report Server's built-in security system with your
own: who is a valid user, what they may do, and where users, groups and roles come from.
Interfaces live in `jet.server.api.custom.security`.

Primary source: [Customized Implementation of the Security API (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741363965079-customized-implementation-of-the-security-api.md).
Era: `logi-report-v17-v19`. The v15 article is
[Customized Implementation of the Security API (Logi JReport)](../docs/jreport-v15-v16/working-with-apis-logi-jreport-server-v15/1500009668781-customized-implementation-of-the-security-api.md).

## The pieces, and which layer each sits in

| Concern | Type | Named methods |
| --- | --- | --- |
| Is this a real user | `jet.server.api.custom.security.AuthenticationProvider` | `isValidUser()` |
| May this user do this | `jet.server.api.custom.security.AuthorizationProvider` | `isBasePermissionOk()` |
| Built-in authorisation | `jet.server.api.Authenticator` | `isValidUser()`, `isPermissionOK()`, `isValidAdminUser()` |
| Create principals | `jet.server.api.admin.SecurityAdminService` | `addRole()`, `addGroup()`, `addUser()` |
| Web page access control | `jet.server.api.http.HttpUtil` | `checkLogin()` |
| Web session management | `jet.server.api.http.HttpUserSessionManager` | `checkLogin()`, `sendUnauthorizedResponse()`, `setHttpExternalAuthorized()` |
| Single sign-on | `jet.server.api.http.HttpExternalAuthorized` | `getExternalAuthorizedUser()`, `handleUnauthorizedRequest()` |

Source for the table: [Tour of the Java API (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741408065175-tour-of-the-java-api.md).

## Implementation rules

- `AuthenticationProvider` is the core interface and must be implemented. It is loaded
  first when the server loads a customised Security API.
- `PermissionProvider` and `PrivilegeProvider` depend on the matching principal provider.
  A custom `UserPermissionProvider` requires a custom `UserProvider`.
- `RelationProvider` depends on both principal interfaces. A custom
  `GroupUserRelationProvider` requires custom `UserProvider` and `GroupProvider`.
- If you implement only part of the API, the server fills the gaps with its own
  implementations of `AuthorizationProvider`, `UserProvider`, `GroupProvider`,
  `RoleProvider`, `GroupUserRelationProvider`, `RoleGroupRelationProvider` and
  `RoleUserRelationProvider`.
- One asymmetry to watch: supplying a `PermissionProvider` or `PrivilegeProvider` without
  an `AuthorizationProvider` gets you the built-in `AuthorizationProvider`, but supplying
  an `AuthorizationProvider` without a permission or privilege provider does **not** get
  you built-in permission or privilege providers.

## Partial implementations the docs endorse

- Custom authentication and authorisation only: `AuthenticationProvider` plus
  `AuthorizationProvider`.
- Custom authentication and users: `AuthenticationProvider` plus `UserProvider`.
- Record level and column level security: you must supply user and role information, so
  `AuthenticationProvider`, `UserProvider`, `RoleProvider` and `RoleUserRelationProvider`.

## Registering the implementation

Classes are declared in `<install_root>\bin\customizedAPI.xml`, which the server reads at
load time. The shape is `<jreport-customized-api><security>` containing
`<authentication-provider>`, `<authorization-provider>`, then `<user>`, `<group>` and
`<role>` blocks each holding `<provider>`, `<permission-provider>` and
`<privilege-provider>`, then a `<relation>` block. The element name in the root is
`jreport-customized-api`, which still carries the pre-rename product name.

## Single sign-on

Access control to Logi Report web pages runs on `checkLogin()`. Without SSO the browser is
challenged with HTTP 401 on the first Logi Report page in a session. Implementing
`HttpExternalAuthorized` lets your application declare who is already signed in, and lets
you redirect an unauthenticated visitor into your own sign-in flow instead of the 401.

Turn it on either way:

- system property at JVM start, for example
  `-Djrs.httpExternalAuthorized=CustomHttpExternalAuthorized`
- API call, `HttpUserSessionManager.setHttpExternalAuthorized()`, where passing null turns
  SSO off again

Turn it on in the JVM where the JSP pages run. If the web server is separate from a
dedicated back end server, that is the web server machine; access to the back end goes over
RMI, which uses neither `checkLogin()` nor SSO.

The docs are blunt about the limits of the `checkLogin()` protocol: credentials travel in
the HTTP request in an insecure stream, so anything outside a firewall needs https.

Sample code: `APISecurity\SingleSignOn\CustomHttpExternalAuthorized.java`, and
`APISecurity\SingleSignOn\com\example\MyExternalAuthorized.java`, which is written as a
multi-tier package. The first cannot be registered from a JSP page because of JSP parser
limitations; the package form can be registered in every case. See
[API Demos (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741407991063-api-demos.md)
for the full sample inventory, including the `LoginLogout` JSP set that demonstrates both
`checkLogin()` variants.

## Do not edit the security tables directly

Users, groups and roles live in the server DBMS, and the running server caches security
information. Updates made outside the API are ignored until restart. Use
`SecurityAdminService`.

## Dynamic Security API

Separate surface, for [dynamic security](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741415142807-dynamic-security-api.md)
objects rather than principals. Methods named: `getDynamicSecurities`,
`addDynamicSecurity`, `deleteDynamicSecurity`, `getCatalogPath`, `getSecurityFileName`,
`getSecurityFile`, `setSecurityFile`, `setDefault`, plus the constant
`APIConst.TAG_SECURITY_FILE_NAME` which defines the security at run time. The equivalent
URL property is `jrs.security_file_name`, which swaps the catalog's security definitions
for those in a named security file.

## Security Context Support

A distinct set of interfaces supporting Unify NXJ Security Context, letting NXJ developers
read user profile information from the security database instead of using the Logi Report
security system.

- `jet.acl.api.JRSecurityContextFactory` with
  `getSecurityContext(javax.swing.JFrame frame, java.util.Vector roles)`, where roles is the
  RLS role list
- `jet.server.api.SecurityContextFactory` with
  `getSecurityContext(String realmName, String userName, String resource, int versionNumber)`,
  returning the security context of one resource
- `jet.server.api.SecurityContext`
- `jet.datasource.JRSecurityUserDataSource` with
  `getResultSet(SecurityContext sc, String param)`
- `jet.datasource.JRSecurityHierarchicalDataSource` with
  `getHierarchicalDataset(SecurityContext sc, String param)`

Source: [Security Context Support (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741407929623-security-context-support.md).
This one is present in every era, including
[v15](../docs/jreport-v15-v16/working-with-apis-logi-jreport-server-v15/1500009643542-security-context-support.md)
and [v16](../docs/jreport-v15-v16/working-with-apis-logi-jreport-server-v16/1500009711881-security-context-support.md).

## Security cache

The server caches security information; how that cache behaves is configured, not coded.
See [Configuring the Security Cache System (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741400164119-configuring-the-security-cache-system.md).

## Era note

The security interface names and the `customizedAPI.xml` mechanism are the same in the v15
and v19 articles. The corpus gives no evidence of a breaking change to this surface across
the rename.
