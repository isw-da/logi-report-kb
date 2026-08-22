---
title: "New Organization Dialog Box Properties"
id: 45203926586253
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203926586253-New-Organization-Dialog-Box-Properties
updated_at: 2026-07-30T20:30:43Z
source_host: logi-report-v26.insightsoftware.com
---
# 
New Organization Dialog Box Properties

This topic describes how you can use the New Organization dialog box to create an organization. 

Server displays the dialog box when an administrator selects New Organization in the Administration > Security > Organization page on the Server Console.

Organization Name

Specify the name of the organization. The system wide organization name is System, which is reserved. The organization name should be distinct. A valid name can contain only '0' to '9', 'a' to 'z', 'A' to 'Z', '&', '-', '_', '.', and blank, with no more than 32 characters.

Max Number of Users

Specify the maximum number of users you want to allow in the organization. The default value unlimited means that the number is not limited. You can select a value from the drop-down list or type an integer number in the combo box directly.

Description

  Provide information about the organization.

Import from Composer checkbox
        

- Check it to show the Composer information.

- Clear it to hide the Composer information.

Server URL

Composer Server base URL.

User Name

Composer Server user name.

Tenant

Composer account/tenant name.

Default User Password

Initial password for newly imported Server users. It may be blank; otherwise, it must contain at least six characters.

Confirm User Password

Must match Default User Password.

Organization Name is required. If it already exists, stop the import and ask the user to log in to that Organization and use the update entry.

OK

  Select to create the organization. 

Cancel

Select to close the dialog box without creating an organization. 

Help

Select to view information about the dialog box.

### User Page

- Add Import From Composer after the existing New User button.

- Clicking Import From Composer opens the Update Organization from Composer dialog.

### Update Organization from Composer Dialog

| Option | Description |
| --- | --- |
| Target Organization | Select the Logi Report Organization to update. Imported users and groups are created only inside this Organization. System administrator: Displays an Organization selector. The administrator can select System or an existing Organization as the import target. Select System to import Composer users and groups into the System security scope. Select an Organization to import them only into that Organization. Organization user/administrator: Displays the current Organization as a read-only value. The user cannot select another Organization, and all imported users, groups, and memberships are restricted to the current Organization. |
| Server URL | Input the Composer Server base URL. |
| User Name | Input the Composer user used for trusted-access authentication. |
| Tenant | Input the Composer account/tenant name to import. |
| Default User Password | Set the initial password for newly imported Logi Report users. Existing user passwords are not changed. |
| Confirm User Password | Re-enter the default password. It must match Default User Password. |
| User Conflict Solution | Skip: Keep the existing Server user without changes. Merge: Update supported Composer properties while retaining Server-specific settings. Replace: Update Full Name and Email while retaining password and other Server security settings. |
| Group Conflict Solution | Skip: Keep the existing group and do not import memberships into it. Merge: Add missing memberships without deleting existing members. Replace: Currently uses the same non-destructive behavior as Merge; existing members are not removed. |
| Import | Validates the inputs and imports Composer users, groups, and memberships into the selected Organization. |
| Cancel | Closes the dialog without importing data. |

### Composer Import Result Dialog

The dialog is displayed after the import completes or terminates.
