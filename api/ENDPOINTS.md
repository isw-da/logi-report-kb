# Logi Report Server RESTful Web API — endpoint index

Source: `logireportserver.yaml` (Swagger 2.0, title "Logi Report Server"). 225 operations across 11 tags.

The spec ships inside the product at `<install_root>/help/webapi/logireportserver.yaml`.
A running server serves it at `/servlet/sendfile/help/webapi/logireportserver.yaml`,
with rendered documentation at `/servlet/sendfile/help/webapi/webapi-docs/index.html`.
Only the JavaScript client is pre-generated (`help/webapi/client-js/`); Java, .NET
and C++ clients are generated from the yaml.

The API is NOT served at `/jinfonet/api`. That path returns 404, which is an easy
way to conclude wrongly that Logi Report has no REST API.

Prose reference for each API family: `rest-web-api.md` and its siblings in this directory.

## Security (66)

- `DELETE /alias/group` — Delete resource aliases of the group.
- `GET /alias/group` — Get the resource aliases of the group.
- `POST /alias/group` — Set resource aliases for the group.
- `PUT /alias/group` — Update resource aliases of the group.
- `DELETE /alias/role` — Delete resource aliases of the role.
- `GET /alias/role` — Get the resource aliases of the role.
- `POST /alias/role` — Set resource aliases for the role.
- `PUT /alias/role` — Update resource aliases of the role.
- `DELETE /alias/user` — Delete resource aliases of the user.
- `GET /alias/user` — Get the resource aliases of the user.
- `POST /alias/user` — Set resource aliases for the user.
- `PUT /alias/user` — Update resource aliases of the user.
- `DELETE /group` — Delete a group.
- `DELETE /group/members` — Delete the group members.
- `GET /group/members` — Get the group members.
- `POST /group/members` — Add group members.
- `GET /group/privileges` — Get the group privileges.
- `PUT /group/privileges` — Update the group privileges.
- `GET /groups` — Get the group list.
- `POST /groups` — Create a new group.
- `POST /ldap/import` — Import users and groups from LDAP server.
- `DELETE /ldap/rolemap` — Delete an LDAP role map.
- `GET /ldap/rolemap` — Get an LDAP role map.
- `PUT /ldap/rolemap` — Edit an LDAP role map.
- `GET /ldap/rolemaps` — Get LDAP role maps.
- `POST /ldap/rolemaps` — Add an LDAP role map.
- `GET /ldap/server` — Get LDAP server setting.
- `PUT /ldap/server` — Set LDAP server setting.
- `GET /ldap/synchronize` — Get LDAP synchronization schedule setting.
- `PUT /ldap/synchronize` — Set LDAP synchronization schedule setting.
- `GET /ldap/synchronize/detail` — Get LDAP synchronization detail.
- `PUT /ldap/synchronize/disable` — Disable LDAP synchronization schedule.
- `PUT /ldap/synchronize/enable` — Enable LDAP synchronization schedule.
- `DELETE /organization` — Delete an organization.
- `GET /organization` — Get an organization.
- `PUT /organization` — Modify an organization.
- `GET /organization/export` — export all stuff for an organization, includes resources/pricipals/permissions/etc.
- `POST /organization/import` — Upload Zip file and import organization, includes resources/pricipals/permissions/etc.
- `GET /organization/resource` — Get the resource allocation of an organization.
- `PUT /organization/resource` — Modify the resource allocation of an organization.
- `GET /organizations` — Get the organization list.
- `POST /organizations` — Add an organization.
- `POST /organizations/composer` — Create an organization and import its users, groups, and memberships from Composer.
- `DELETE /role` — Delete a role.
- `DELETE /role/members` — Delete the role members.
- `GET /role/members` — Get the members.
- `POST /role/members` — Add the role members.
- `GET /role/privileges` — Get the role privileges.
- `PUT /role/privileges` — Update the role privileges.
- `GET /roles` — Get the role list.
- `POST /roles` — Create a new role.
- `DELETE /user` — Delete a user account.
- `GET /user` — Get the user properties.
- `PUT /user` — Update the user properties.
- `DELETE /user/groups` — Delete the groups from the user.
- `GET /user/groups` — Get the groups of the user.
- `POST /user/groups` — Add the groups to the user.
- `PUT /user/password` — Change a user's password.
- `GET /user/privileges` — Get the user privileges.
- `PUT /user/privileges` — Update the user privileges.
- `DELETE /user/roles` — Delete the roles from the user.
- `GET /user/roles` — Get the roles of the user.
- `POST /user/roles` — Add the roles to the user.
- `GET /users` — Get the user list.
- `POST /users` — Create a new user.
- `POST /users/composer` — Import Composer users, groups, and memberships into the current organization scope.

## Configuration (43)

- `DELETE /dynamic/connection` — Delete the dynamic connection.
- `GET /dynamic/connection` — Get the properties of the dynamic connection.
- `PUT /dynamic/connection` — Update the properties of the dynamic connection.
- `GET /dynamic/connections` — Get dynamic connection records.
- `POST /dynamic/connections` — Add a dynamic connection.
- `DELETE /dynamic/displayname` — Delete the dynamic display name.
- `GET /dynamic/displayname` — Get the properties of the dynamic display name.
- `PUT /dynamic/displayname` — Update the properties of the dynamic display name.
- `GET /dynamic/displaynames` — Get dynamic display name records.
- `POST /dynamic/displaynames` — Add a dynamic display name.
- `GET /dynamic/securities` — Get dynamic security records.
- `POST /dynamic/securities` — Add a dynamic security.
- `DELETE /dynamic/security` — Delete the dynamic security.
- `GET /dynamic/security` — Get the properties of the dynamic security.
- `PUT /dynamic/security` — Update the properties of the dynamic security.
- `GET /preference/default/server` — Get the default preference of the server.
- `PUT /preference/default/server` — Set the default preference of the server.
- `GET /preference/default/viewer` — Get the default preference of Logi Report Viewer.
- `PUT /preference/default/viewer` — Set the default preference of Logi Report Viewer.
- `GET /preference/server` — Get the user preference of the server.
- `PUT /preference/server` — Set the user preference of the server.
- `GET /preference/viewer` — Get the user preference of Logi Report Viewer.
- `PUT /preference/viewer` — Set the user preference of Logi Report Viewer.
- `DELETE /profile/catalog` — Delete the profile.
- `GET /profile/catalog` — Get the properties of the profile.
- `PUT /profile/catalog` — Update the properties of the profile.
- `DELETE /profile/dashboard` — Delete the profile.
- `GET /profile/dashboard` — Get the properties of the profile.
- `PUT /profile/dashboard` — Update the properties of the profile.
- `DELETE /profile/pagestudio` — Delete the profile.
- `GET /profile/pagestudio` — Get the properties of the profile.
- `PUT /profile/pagestudio` — Update the properties of the profile.
- `DELETE /profile/webstudio` — Delete the profile.
- `GET /profile/webstudio` — Get the properties of the profile.
- `PUT /profile/webstudio` — Update the properties of the profile.
- `GET /profilelist/catalog` — Get the profiles.
- `POST /profilelist/catalog` — Add a profile.
- `GET /profilelist/dashboard` — Get the profiles.
- `POST /profilelist/dashboard` — Add a profile.
- `GET /profilelist/pagestudio` — Get the profiles.
- `POST /profilelist/pagestudio` — Add a profile.
- `GET /profilelist/webstudio` — Get the profiles.
- `POST /profilelist/webstudio` — Add a profile.

## Resource Tree (28)

- `DELETE /node` — Delete the node by the server resource path.
- `GET /node` — Get the node properties by the server resource path.
- `PUT /node` — Set the node properties by the server resource path.
- `GET /node/inheritedPermissions` — Get inherited permissions on the node for principals.
- `GET /node/permission` — >-
- `DELETE /node/permissions` — Delete principals' permissions on the node/version.
- `GET /node/permissions` — >-
- `PUT /node/permissions` — Set principals' permissions on the node/version.
- `GET /node/rptcatrelation` — Get relations between report and catalog when report is saved as in page report studio/web report studio
- `GET /node/shared` — Get the shared node information by the shared node path.
- `PUT /node/shared` — Update the shared node information by the shared node path.
- `GET /nodes` — Get the nodes in a folder and filter by specified node types.
- `POST /nodes` — Upload Zip file and publish new resource. For creating new folder, no need to upload file
- `POST /nodes/download` — Download resources
- `GET /nodes/list` — Get the node name list in a folder and filter by specified node types.
- `POST /nodes/product` — >-
- `POST /nodes/server` — Publish new resource from server machine.
- `GET /nodes/shared` — Get the shared node informations.
- `POST /nodes/shared` — Create shared nodes.
- `DELETE /reports/embeddedImage` — clear embedded images from reports
- `POST /reports/embeddedImage` — embed images into reports
- `GET /resultVersion` — Get the properties of a report result version by the version number.
- `GET /resultVersions` — Get the result versions of a report resource.
- `GET /resultVersions/list` — Get the result version number list of a report resource.
- `GET /tree` — Get the resource tree full list with node properties according to additional conditions.
- `GET /version` — Get the properties of a version by the version number.
- `GET /versions` — Get the versions of a server resource.
- `GET /versions/list` — Get the version number list of a server resource.

## Task (27)

- `POST /file` — Upload private key or other file to server.
- `DELETE /myTasks/completed` — Delete completed task records.
- `GET /myTasks/completed` — Get completed task records.
- `GET /myTasks/completed/page` — Get paged completed task records.
- `DELETE /myTasks/interactive/list` — Delete some interactive task records from the list corresponding to "/myTasks/interactive/list" which contains the records both in progress and finished.
- `GET /myTasks/interactive/list` — Get all the interactive task records. Every task record here comes from direct Page/Web Studio run (shown in the Interactive tab of My Tasks tab in the server console) and may be in progress or may have finished.
- `DELETE /myTasks/interactive/list/inProgress` — Kill some interactive task records from the list corresponding to "/myTasks/interactive/list/inProgress" which only contains the records in progress. This list is different from another list corresponding to "/myTasks/interactive/list" which contains the records both in progress and finished.
- `POST /myTasks/ondemand` — View a report task.
- `DELETE /myTasks/ondemand/list` — Delete some on demand task records. Every task record here comes from Advanced Run (shown in the Background Tasks tab of My Tasks tab in the server console) and may be in progress or may have finished.
- `GET /myTasks/ondemand/list` — Get all the ondemand task records. Every task record here comes from Advanced Run (shown in the Background Tasks tab of My Tasks tab in the server console) and may be in progress or may have finished.
- `DELETE /myTasks/running/list` — Kill some running task records. Every task record here comes from Schedule or Bursting (shown in the My Tasks > Running tab in the server console) and is in progress.
- `GET /myTasks/running/list` — Get all the running task records. Every task record here comes from Schedule or Bursting (shown in the Running tab of My Tasks tab in the server console) and is in progress.
- `DELETE /myTasks/scheduled` — Delete a scheduled task.
- `GET /myTasks/scheduled` — Get scheduled task.
- `POST /myTasks/scheduled` — Submit a scheduled task.
- `PUT /myTasks/scheduled` — Modify an existing scheduled task. Only need to specify task properties which you want to change.
- `POST /myTasks/scheduled/copy` — Copy a scheduled task as a new one.
- `PUT /myTasks/scheduled/disable` — Disable a scheduled task.
- `PUT /myTasks/scheduled/enable` — Enable a scheduled task.
- `GET /myTasks/scheduled/list` — Get scheduled tasks.
- `GET /myTasks/scheduled/list/id` — Get scheduled taskID list.
- `GET /myTasks/scheduled/list/page` — Get paged scheduled tasks.
- `PUT /myTasks/scheduled/run` — Run a scheduled task immediately.
- `GET /myTasks/scheduled/script` — Export scheduled tasks to task script.
- `POST /myTasks/scheduled/script` — Import scheduled tasks from an exported task script.
- `POST /report/parameterInfos` — Get the list of report parameter info for schedule and on-demand run.
- `GET /report/reportTabs` — Get the list of report tabs for schedule and on-demand run.

## BV (22)

- `GET /BV/aggregations` — Get the aggregations in the business view.
- `GET /BV/categories` — Get the categories in the business view.
- `GET /BV/details` — Get the detail objects in the business view.
- `GET /BV/dimension` — Get the group object in the business view.
- `GET /BV/dimension/permission` — Get the permission of a group object.
- `PUT /BV/dimension/permission` — Set the permission of a group object.
- `DELETE /BV/dimension/permissions` — Delete group object permissions in a business view.
- `GET /BV/dimension/permissions` — Get group object permissions in a business view.
- `PUT /BV/dimension/permissions` — Set group object permissions in a business view.
- `GET /BV/dimensions` — Get the group objects in the business view.
- `DELETE /BV/dynamic-securities` — Delete the permissions of the BV with specified dynamic security ID.
- `GET /BV/dynamic-securities` — Return the permissions of the BV with specified dynamic security ID.
- `PUT /BV/dynamic-securities` — Set the permissions of the BV with specified dynamic security ID.
- `GET /BV/dynamic-security` — Return the permission of the BV field with specified dynamic security ID.
- `PUT /BV/dynamic-security` — Set the permission of the BV field with specified dynamic security ID.
- `DELETE /BV/permissions` — Delete principals' permissions on BVs in catalog by Setting Name.
- `GET /BV/permissions` — >-
- `PUT /BV/permissions` — Set principals' permissions on BVs in catalog.
- `GET /BVs` — Get the business views in a catalog.
- `DELETE /report/BVList` — Delete the list of report available BV.
- `GET /report/BVList` — Get the list of report available BV.
- `PUT /report/BVList` — Set the list of report available BV.

## Bookmark (9)

- `DELETE /bookmark` — Delete a bookmark.
- `GET /bookmark` — Get a bookmark.
- `PUT /bookmark` — Update a bookmark.
- `GET /bookmark/default` — Get a default bookmark.
- `PUT /bookmark/default/clear` — Clear default bookmark.
- `PUT /bookmark/default/set` — Set default bookmark.
- `GET /bookmark/names` — Get the names of bookmarks.
- `GET /bookmarks` — Get bookmarks.
- `POST /bookmarks` — Add a bookmark.

## NLS (9)

- `DELETE /nls/catalog` — Delete nls setting of a catalog.
- `GET /nls/catalog` — Get nls setting of a catalog.
- `PUT /nls/catalog` — Update nls setting of a catalog.
- `DELETE /nls/global` — Delete global nls setting.
- `GET /nls/global` — Get global nls setting.
- `PUT /nls/global` — Update global nls setting.
- `DELETE /nls/report` — Delete nls setting of a page/web report, lc, dashboard.
- `GET /nls/report` — Get nls setting of a page/web report, lc, dashboard.
- `PUT /nls/report` — Update nls setting of a page/web report, lc, dashboard.

## ReportParamList (7)

- `DELETE /reportParamList` — Delete a ReportParamList.
- `GET /reportParamList` — Get a ReportParamList.
- `GET /reportParamList/default` — Get default ReportParamList.
- `GET /reportParamList/showParamPage` — Get showParamPage.
- `PUT /reportParamList/showParamPage` — Get default.
- `GET /reportParamLists` — Get the ReportParamLists of specified type.
- `POST /reportParamLists`

## Trigger (7)

- `DELETE /trigger` — Delete a trigger.
- `GET /trigger` — Get a trigger.
- `PUT /trigger/disable` — Disable a trigger.
- `PUT /trigger/enable` — Enable a trigger.
- `PUT /trigger/fire` — Fire a trigger.
- `GET /triggers` — Get all triggers.
- `POST /triggers` — Create a trigger.

## User Session (5)

- `DELETE /session` — Delete the current user session (logout).
- `GET /session` — Get the current user session.
- `POST /session` — Create new user session (login).
- `PUT /session/timeout` — >-
- `POST /session/token/refresh` — Refresh user session tokens.

## Single Sign On (2)

- `POST /sso/register` — Generate alternative id to be used in POST /sso/token call later. Only system admin user is permitted to call it. It is available only when built-in SSO takes effect
- `POST /sso/token` — Generate token to be verified in built-in Single Sign On. It is available only when built-in SSO takes effect
