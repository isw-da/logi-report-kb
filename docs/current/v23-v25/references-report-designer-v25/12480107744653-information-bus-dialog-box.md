---
title: "Information Bus Dialog Box"
id: 12480107744653
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480107744653-Information-Bus-Dialog-Box
updated_at: 2026-02-25T23:49:14Z
source_host: docs-report.zendesk.com
---
# 
Information Bus Dialog Box

You can use the Information Bus dialog box to edit the Information Bus content that Designer saves with user information in the current catalog. This topic describes the options in the dialog box.
    

Designer displays the Information Bus dialog box when you navigate to File > Information Bus. 

Information Bus is a built-in object in Report containing information from information containers of three levels: global level, organization level, and user level. System admin can get or put information in all information containers. Organization admin can get or put information in the global level information container, its own organization level information container, and the user level information containers that belong to its organization. Organization user can get or put information in the global level information container, the organization level information container it belongs, and its own user level information container.

Designer displays these options:

Information container list 

This box shows a tree structure according to the user definition in the information containers in the current catalog. The users here are the same as those for business view security.

Information box

This box displays the information created for the selected information container, which are key-value pairs of information that authorized users can put or get by  calling APIs and writing formulas with the following functions: 

- GetInfo()

- GetOrgInfo()

- GetUserInfo()

- PutInfo()

- PutOrgInfo()

- PutUserInfo()

- RemoveInfo()

- RemoveOrgInfo()

- RemoveUserInfo()

To edit information for a container, select it from the container list, select Add above the information box, and then double-click the Key and Value cells to specify the key and value respectively. To remove an information line, select it and select Remove.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
