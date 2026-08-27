# Logi Report Server Web API — endpoint index

Source: `logireportserver.yaml`, shipped inside Logi Report Server at
`/opt/LogiReport/Server/help/webapi/logireportserver.yaml` and served by the
bundled Swagger UI at `/help/webapi/webapi-docs/`. Extracted from a running
**Logi Report Server 1.3.0** instance (product build 26.2 SP1).

**225 operations across 11 tags, over 124 paths.**

Spec format: **Swagger 2.0**. Note this differs from Composer, whose spec is
OpenAPI 3.1.0 (`si-docs-mirror/composer-api/composer-openapi.json`). Any tool
consuming both must handle the two formats, or convert. Machine-readable copies
here: `spec/logireport-openapi.yaml` and `spec/logireport-openapi.json`.

All paths below are shown with the spec's `basePath` (`/jrserver/api/v1.2`) applied.

## Bookmark

- `DELETE /jrserver/api/v1.2/bookmark` — Delete a bookmark.
- `GET /jrserver/api/v1.2/bookmark` — Get a bookmark.
- `PUT /jrserver/api/v1.2/bookmark` — Update a bookmark.
- `GET /jrserver/api/v1.2/bookmark/default` — Get a default bookmark.
- `PUT /jrserver/api/v1.2/bookmark/default/clear` — Clear default bookmark.
- `PUT /jrserver/api/v1.2/bookmark/default/set` — Set default bookmark.
- `GET /jrserver/api/v1.2/bookmark/names` — Get the names of bookmarks.
- `GET /jrserver/api/v1.2/bookmarks` — Get bookmarks.
- `POST /jrserver/api/v1.2/bookmarks` — Add a bookmark.

## BV

- `GET /jrserver/api/v1.2/BV/aggregations` — Get the aggregations in the business view.
- `GET /jrserver/api/v1.2/BV/categories` — Get the categories in the business view.
- `GET /jrserver/api/v1.2/BV/details` — Get the detail objects in the business view.
- `GET /jrserver/api/v1.2/BV/dimension` — Get the group object in the business view.
- `GET /jrserver/api/v1.2/BV/dimension/permission` — Get the permission of a group object.
- `PUT /jrserver/api/v1.2/BV/dimension/permission` — Set the permission of a group object.
- `DELETE /jrserver/api/v1.2/BV/dimension/permissions` — Delete group object permissions in a business view.
- `GET /jrserver/api/v1.2/BV/dimension/permissions` — Get group object permissions in a business view.
- `PUT /jrserver/api/v1.2/BV/dimension/permissions` — Set group object permissions in a business view.
- `GET /jrserver/api/v1.2/BV/dimensions` — Get the group objects in the business view.
- `DELETE /jrserver/api/v1.2/BV/dynamic-securities` — Delete the permissions of the BV with specified dynamic security ID.
- `GET /jrserver/api/v1.2/BV/dynamic-securities` — Return the permissions of the BV with specified dynamic security ID.
- `PUT /jrserver/api/v1.2/BV/dynamic-securities` — Set the permissions of the BV with specified dynamic security ID.
- `GET /jrserver/api/v1.2/BV/dynamic-security` — Return the permission of the BV field with specified dynamic security ID.
- `PUT /jrserver/api/v1.2/BV/dynamic-security` — Set the permission of the BV field with specified dynamic security ID.
- `DELETE /jrserver/api/v1.2/BV/permissions` — Delete principals' permissions on BVs in catalog by Setting Name.
- `GET /jrserver/api/v1.2/BV/permissions` — Get principals' permissions on BVs in catalog.
- `PUT /jrserver/api/v1.2/BV/permissions` — Set principals' permissions on BVs in catalog.
- `GET /jrserver/api/v1.2/BVs` — Get the business views in a catalog.
- `DELETE /jrserver/api/v1.2/report/BVList` — Delete the list of report available BV.
- `GET /jrserver/api/v1.2/report/BVList` — Get the list of report available BV.
- `PUT /jrserver/api/v1.2/report/BVList` — Set the list of report available BV.

## Configuration

- `DELETE /jrserver/api/v1.2/dynamic/connection` — Delete the dynamic connection.
- `GET /jrserver/api/v1.2/dynamic/connection` — Get the properties of the dynamic connection.
- `PUT /jrserver/api/v1.2/dynamic/connection` — Update the properties of the dynamic connection.
- `GET /jrserver/api/v1.2/dynamic/connections` — Get dynamic connection records.
- `POST /jrserver/api/v1.2/dynamic/connections` — Add a dynamic connection.
- `DELETE /jrserver/api/v1.2/dynamic/displayname` — Delete the dynamic display name.
- `GET /jrserver/api/v1.2/dynamic/displayname` — Get the properties of the dynamic display name.
- `PUT /jrserver/api/v1.2/dynamic/displayname` — Update the properties of the dynamic display name.
- `GET /jrserver/api/v1.2/dynamic/displaynames` — Get dynamic display name records.
- `POST /jrserver/api/v1.2/dynamic/displaynames` — Add a dynamic display name.
- `GET /jrserver/api/v1.2/dynamic/securities` — Get dynamic security records.
- `POST /jrserver/api/v1.2/dynamic/securities` — Add a dynamic security.
- `DELETE /jrserver/api/v1.2/dynamic/security` — Delete the dynamic security.
- `GET /jrserver/api/v1.2/dynamic/security` — Get the properties of the dynamic security.
- `PUT /jrserver/api/v1.2/dynamic/security` — Update the properties of the dynamic security.
- `GET /jrserver/api/v1.2/preference/default/server` — Get the default preference of the server.
- `PUT /jrserver/api/v1.2/preference/default/server` — Set the default preference of the server.
- `GET /jrserver/api/v1.2/preference/default/viewer` — Get the default preference of Logi Report Viewer.
- `PUT /jrserver/api/v1.2/preference/default/viewer` — Set the default preference of Logi Report Viewer.
- `GET /jrserver/api/v1.2/preference/server` — Get the user preference of the server.
- `PUT /jrserver/api/v1.2/preference/server` — Set the user preference of the server.
- `GET /jrserver/api/v1.2/preference/viewer` — Get the user preference of Logi Report Viewer.
- `PUT /jrserver/api/v1.2/preference/viewer` — Set the user preference of Logi Report Viewer.
- `DELETE /jrserver/api/v1.2/profile/catalog` — Delete the profile.
- `GET /jrserver/api/v1.2/profile/catalog` — Get the properties of the profile.
- `PUT /jrserver/api/v1.2/profile/catalog` — Update the properties of the profile.
- `DELETE /jrserver/api/v1.2/profile/dashboard` — Delete the profile.
- `GET /jrserver/api/v1.2/profile/dashboard` — Get the properties of the profile.
- `PUT /jrserver/api/v1.2/profile/dashboard` — Update the properties of the profile.
- `DELETE /jrserver/api/v1.2/profile/pagestudio` — Delete the profile.
- `GET /jrserver/api/v1.2/profile/pagestudio` — Get the properties of the profile.
- `PUT /jrserver/api/v1.2/profile/pagestudio` — Update the properties of the profile.
- `DELETE /jrserver/api/v1.2/profile/webstudio` — Delete the profile.
- `GET /jrserver/api/v1.2/profile/webstudio` — Get the properties of the profile.
- `PUT /jrserver/api/v1.2/profile/webstudio` — Update the properties of the profile.
- `GET /jrserver/api/v1.2/profilelist/catalog` — Get the profiles.
- `POST /jrserver/api/v1.2/profilelist/catalog` — Add a profile.
- `GET /jrserver/api/v1.2/profilelist/dashboard` — Get the profiles.
- `POST /jrserver/api/v1.2/profilelist/dashboard` — Add a profile.
- `GET /jrserver/api/v1.2/profilelist/pagestudio` — Get the profiles.
- `POST /jrserver/api/v1.2/profilelist/pagestudio` — Add a profile.
- `GET /jrserver/api/v1.2/profilelist/webstudio` — Get the profiles.
- `POST /jrserver/api/v1.2/profilelist/webstudio` — Add a profile.

## NLS

- `DELETE /jrserver/api/v1.2/nls/catalog` — Delete nls setting of a catalog.
- `GET /jrserver/api/v1.2/nls/catalog` — Get nls setting of a catalog.
- `PUT /jrserver/api/v1.2/nls/catalog` — Update nls setting of a catalog.
- `DELETE /jrserver/api/v1.2/nls/global` — Delete global nls setting.
- `GET /jrserver/api/v1.2/nls/global` — Get global nls setting.
- `PUT /jrserver/api/v1.2/nls/global` — Update global nls setting.
- `DELETE /jrserver/api/v1.2/nls/report` — Delete nls setting of a page/web report, lc, dashboard.
- `GET /jrserver/api/v1.2/nls/report` — Get nls setting of a page/web report, lc, dashboard.
- `PUT /jrserver/api/v1.2/nls/report` — Update nls setting of a page/web report, lc, dashboard.

## ReportParamList

- `DELETE /jrserver/api/v1.2/reportParamList` — Delete a ReportParamList.
- `GET /jrserver/api/v1.2/reportParamList` — Get a ReportParamList.
- `GET /jrserver/api/v1.2/reportParamList/default` — Get default ReportParamList.
- `GET /jrserver/api/v1.2/reportParamList/showParamPage` — Get showParamPage.
- `PUT /jrserver/api/v1.2/reportParamList/showParamPage` — Get default.
- `GET /jrserver/api/v1.2/reportParamLists` — Get the ReportParamLists of specified type.
- `POST /jrserver/api/v1.2/reportParamLists` — Save ReportParamList

## Resource Tree

- `DELETE /jrserver/api/v1.2/node` — Delete the node by the server resource path.
- `GET /jrserver/api/v1.2/node` — Get the node properties by the server resource path.
- `PUT /jrserver/api/v1.2/node` — Set the node properties by the server resource path.
- `GET /jrserver/api/v1.2/node/inheritedPermissions` — Get inherited permissions on the node for principals.
- `GET /jrserver/api/v1.2/node/permission` — Get permission of node/version by the server resource path for the specified user. If the userName is not specified then return permission of the user of the user session.
- `DELETE /jrserver/api/v1.2/node/permissions` — Delete principals' permissions on the node/version.
- `GET /jrserver/api/v1.2/node/permissions` — Get principals' permissions on the node/version by the server resource path.
- `PUT /jrserver/api/v1.2/node/permissions` — Set principals' permissions on the node/version.
- `GET /jrserver/api/v1.2/node/rptcatrelation` — Get relations between report and catalog when report is saved as in page report studio/web report studio
- `GET /jrserver/api/v1.2/node/shared` — Get the shared node information by the shared node path.
- `PUT /jrserver/api/v1.2/node/shared` — Update the shared node information by the shared node path.
- `GET /jrserver/api/v1.2/nodes` — Get the nodes in a folder and filter by specified node types.
- `POST /jrserver/api/v1.2/nodes` — Upload Zip file and publish new resource. For creating new folder, no need to upload file
- `POST /jrserver/api/v1.2/nodes/download` — Download resources
- `GET /jrserver/api/v1.2/nodes/list` — Get the node name list in a folder and filter by specified node types.
- `POST /jrserver/api/v1.2/nodes/product` — Publish new resource to product server. The "parentFolder" in "sourceNodes" is the target Server path which will publish to, and "sourcePath" is the Server path which will publish from. So in the sample,  {
- `POST /jrserver/api/v1.2/nodes/server` — Publish new resource from server machine.
- `GET /jrserver/api/v1.2/nodes/shared` — Get the shared node informations.
- `POST /jrserver/api/v1.2/nodes/shared` — Create shared nodes.
- `DELETE /jrserver/api/v1.2/reports/embeddedImage` — clear embedded images from reports
- `POST /jrserver/api/v1.2/reports/embeddedImage` — embed images into reports
- `GET /jrserver/api/v1.2/resultVersion` — Get the properties of a report result version by the version number.
- `GET /jrserver/api/v1.2/resultVersions` — Get the result versions of a report resource.
- `GET /jrserver/api/v1.2/resultVersions/list` — Get the result version number list of a report resource.
- `GET /jrserver/api/v1.2/tree` — Get the resource tree full list with node properties according to additional conditions.
- `GET /jrserver/api/v1.2/version` — Get the properties of a version by the version number.
- `GET /jrserver/api/v1.2/versions` — Get the versions of a server resource.
- `GET /jrserver/api/v1.2/versions/list` — Get the version number list of a server resource.

## Security

- `DELETE /jrserver/api/v1.2/alias/group` — Delete resource aliases of the group.
- `GET /jrserver/api/v1.2/alias/group` — Get the resource aliases of the group.
- `POST /jrserver/api/v1.2/alias/group` — Set resource aliases for the group.
- `PUT /jrserver/api/v1.2/alias/group` — Update resource aliases of the group.
- `DELETE /jrserver/api/v1.2/alias/role` — Delete resource aliases of the role.
- `GET /jrserver/api/v1.2/alias/role` — Get the resource aliases of the role.
- `POST /jrserver/api/v1.2/alias/role` — Set resource aliases for the role.
- `PUT /jrserver/api/v1.2/alias/role` — Update resource aliases of the role.
- `DELETE /jrserver/api/v1.2/alias/user` — Delete resource aliases of the user.
- `GET /jrserver/api/v1.2/alias/user` — Get the resource aliases of the user.
- `POST /jrserver/api/v1.2/alias/user` — Set resource aliases for the user.
- `PUT /jrserver/api/v1.2/alias/user` — Update resource aliases of the user.
- `DELETE /jrserver/api/v1.2/group` — Delete a group.
- `DELETE /jrserver/api/v1.2/group/members` — Delete the group members.
- `GET /jrserver/api/v1.2/group/members` — Get the group members.
- `POST /jrserver/api/v1.2/group/members` — Add group members.
- `GET /jrserver/api/v1.2/group/privileges` — Get the group privileges.
- `PUT /jrserver/api/v1.2/group/privileges` — Update the group privileges.
- `GET /jrserver/api/v1.2/groups` — Get the group list.
- `POST /jrserver/api/v1.2/groups` — Create a new group.
- `POST /jrserver/api/v1.2/ldap/import` — Import users and groups from LDAP server.
- `DELETE /jrserver/api/v1.2/ldap/rolemap` — Delete an LDAP role map.
- `GET /jrserver/api/v1.2/ldap/rolemap` — Get an LDAP role map.
- `PUT /jrserver/api/v1.2/ldap/rolemap` — Edit an LDAP role map.
- `GET /jrserver/api/v1.2/ldap/rolemaps` — Get LDAP role maps.
- `POST /jrserver/api/v1.2/ldap/rolemaps` — Add an LDAP role map.
- `GET /jrserver/api/v1.2/ldap/server` — Get LDAP server setting.
- `PUT /jrserver/api/v1.2/ldap/server` — Set LDAP server setting.
- `GET /jrserver/api/v1.2/ldap/synchronize` — Get LDAP synchronization schedule setting.
- `PUT /jrserver/api/v1.2/ldap/synchronize` — Set LDAP synchronization schedule setting.
- `GET /jrserver/api/v1.2/ldap/synchronize/detail` — Get LDAP synchronization detail.
- `PUT /jrserver/api/v1.2/ldap/synchronize/disable` — Disable LDAP synchronization schedule.
- `PUT /jrserver/api/v1.2/ldap/synchronize/enable` — Enable LDAP synchronization schedule.
- `DELETE /jrserver/api/v1.2/organization` — Delete an organization.
- `GET /jrserver/api/v1.2/organization` — Get an organization.
- `PUT /jrserver/api/v1.2/organization` — Modify an organization.
- `GET /jrserver/api/v1.2/organization/export` — export all stuff for an organization, includes resources/pricipals/permissions/etc.
- `POST /jrserver/api/v1.2/organization/import` — Upload Zip file and import organization, includes resources/pricipals/permissions/etc.
- `GET /jrserver/api/v1.2/organization/resource` — Get the resource allocation of an organization.
- `PUT /jrserver/api/v1.2/organization/resource` — Modify the resource allocation of an organization.
- `GET /jrserver/api/v1.2/organizations` — Get the organization list.
- `POST /jrserver/api/v1.2/organizations` — Add an organization.
- `POST /jrserver/api/v1.2/organizations/composer` — Create an organization and import its users, groups, and memberships from Composer.
- `DELETE /jrserver/api/v1.2/role` — Delete a role.
- `DELETE /jrserver/api/v1.2/role/members` — Delete the role members.
- `GET /jrserver/api/v1.2/role/members` — Get the members.
- `POST /jrserver/api/v1.2/role/members` — Add the role members.
- `GET /jrserver/api/v1.2/role/privileges` — Get the role privileges.
- `PUT /jrserver/api/v1.2/role/privileges` — Update the role privileges.
- `GET /jrserver/api/v1.2/roles` — Get the role list.
- `POST /jrserver/api/v1.2/roles` — Create a new role.
- `DELETE /jrserver/api/v1.2/user` — Delete a user account.
- `GET /jrserver/api/v1.2/user` — Get the user properties.
- `PUT /jrserver/api/v1.2/user` — Update the user properties.
- `DELETE /jrserver/api/v1.2/user/groups` — Delete the groups from the user.
- `GET /jrserver/api/v1.2/user/groups` — Get the groups of the user.
- `POST /jrserver/api/v1.2/user/groups` — Add the groups to the user.
- `PUT /jrserver/api/v1.2/user/password` — Change a user's password.
- `GET /jrserver/api/v1.2/user/privileges` — Get the user privileges.
- `PUT /jrserver/api/v1.2/user/privileges` — Update the user privileges.
- `DELETE /jrserver/api/v1.2/user/roles` — Delete the roles from the user.
- `GET /jrserver/api/v1.2/user/roles` — Get the roles of the user.
- `POST /jrserver/api/v1.2/user/roles` — Add the roles to the user.
- `GET /jrserver/api/v1.2/users` — Get the user list.
- `POST /jrserver/api/v1.2/users` — Create a new user.
- `POST /jrserver/api/v1.2/users/composer` — Import Composer users, groups, and memberships into the current organization scope.

## Single Sign On

- `POST /jrserver/api/v1.2/sso/register` — Generate alternative id to be used in POST /sso/token call later. Only system admin user is permitted to call it. It is available only when built-in SSO takes effect
- `POST /jrserver/api/v1.2/sso/token` — Generate token to be verified in built-in Single Sign On. It is available only when built-in SSO takes effect

## Task

- `POST /jrserver/api/v1.2/file` — Upload private key or other file to server.
- `DELETE /jrserver/api/v1.2/myTasks/completed` — Delete completed task records.
- `GET /jrserver/api/v1.2/myTasks/completed` — Get completed task records.
- `GET /jrserver/api/v1.2/myTasks/completed/page` — Get paged completed task records.
- `DELETE /jrserver/api/v1.2/myTasks/interactive/list` — Delete some interactive task records from the list corresponding to "/myTasks/interactive/list" which contains the records both in progress and finished.
- `GET /jrserver/api/v1.2/myTasks/interactive/list` — Get all the interactive task records. Every task record here comes from direct Page/Web Studio run (shown in the Interactive tab of My Tasks tab in the server console) and may be in progress or may have finished.
- `DELETE /jrserver/api/v1.2/myTasks/interactive/list/inProgress` — Kill some interactive task records from the list corresponding to "/myTasks/interactive/list/inProgress" which only contains the records in progress. This list is different from another list corresponding to "/myTasks/interactive/list" which contains the records both in progress and finished.
- `POST /jrserver/api/v1.2/myTasks/ondemand` — View a report task.
- `DELETE /jrserver/api/v1.2/myTasks/ondemand/list` — Delete some on demand task records. Every task record here comes from Advanced Run (shown in the Background Tasks tab of My Tasks tab in the server console) and may be in progress or may have finished.
- `GET /jrserver/api/v1.2/myTasks/ondemand/list` — Get all the ondemand task records. Every task record here comes from Advanced Run (shown in the Background Tasks tab of My Tasks tab in the server console) and may be in progress or may have finished.
- `DELETE /jrserver/api/v1.2/myTasks/running/list` — Kill some running task records. Every task record here comes from Schedule or Bursting (shown in the My Tasks > Running tab in the server console) and is in progress.
- `GET /jrserver/api/v1.2/myTasks/running/list` — Get all the running task records. Every task record here comes from Schedule or Bursting (shown in the Running tab of My Tasks tab in the server console) and is in progress.
- `DELETE /jrserver/api/v1.2/myTasks/scheduled` — Delete a scheduled task.
- `GET /jrserver/api/v1.2/myTasks/scheduled` — Get scheduled task.
- `POST /jrserver/api/v1.2/myTasks/scheduled` — Submit a scheduled task.
- `PUT /jrserver/api/v1.2/myTasks/scheduled` — Modify an existing scheduled task. Only need to specify task properties which you want to change.
- `POST /jrserver/api/v1.2/myTasks/scheduled/copy` — Copy a scheduled task as a new one.
- `PUT /jrserver/api/v1.2/myTasks/scheduled/disable` — Disable a scheduled task.
- `PUT /jrserver/api/v1.2/myTasks/scheduled/enable` — Enable a scheduled task.
- `GET /jrserver/api/v1.2/myTasks/scheduled/list` — Get scheduled tasks.
- `GET /jrserver/api/v1.2/myTasks/scheduled/list/id` — Get scheduled taskID list.
- `GET /jrserver/api/v1.2/myTasks/scheduled/list/page` — Get paged scheduled tasks.
- `PUT /jrserver/api/v1.2/myTasks/scheduled/run` — Run a scheduled task immediately.
- `GET /jrserver/api/v1.2/myTasks/scheduled/script` — Export scheduled tasks to task script.
- `POST /jrserver/api/v1.2/myTasks/scheduled/script` — Import scheduled tasks from an exported task script.
- `POST /jrserver/api/v1.2/report/parameterInfos` — Get the list of report parameter info for schedule and on-demand run.
- `GET /jrserver/api/v1.2/report/reportTabs` — Get the list of report tabs for schedule and on-demand run.

## Trigger

- `DELETE /jrserver/api/v1.2/trigger` — Delete a trigger.
- `GET /jrserver/api/v1.2/trigger` — Get a trigger.
- `PUT /jrserver/api/v1.2/trigger/disable` — Disable a trigger.
- `PUT /jrserver/api/v1.2/trigger/enable` — Enable a trigger.
- `PUT /jrserver/api/v1.2/trigger/fire` — Fire a trigger.
- `GET /jrserver/api/v1.2/triggers` — Get all triggers.
- `POST /jrserver/api/v1.2/triggers` — Create a trigger.

## User Session

- `DELETE /jrserver/api/v1.2/session` — Delete the current user session (logout).
- `GET /jrserver/api/v1.2/session` — Get the current user session.
- `POST /jrserver/api/v1.2/session` — Create new user session (login).
- `PUT /jrserver/api/v1.2/session/timeout` — Set session timeout in seconds. A negative time indicates the session should never timeout.
- `POST /jrserver/api/v1.2/session/token/refresh` — Refresh user session tokens.
