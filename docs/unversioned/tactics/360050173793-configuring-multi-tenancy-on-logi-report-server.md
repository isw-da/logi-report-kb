---
title: "Configuring Multi-Tenancy on Logi Report Server"
id: 360050173793
section: "Tactics"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360050173793-Configuring-Multi-Tenancy-on-Logi-Report-Server
updated_at: 2022-11-01T03:49:54Z
---

# Configuring Multi-Tenancy on Logi Report Server

Logi Report Server supports a multi-tenant architecture by organizing users into different organizations or tenants. An organization is a group of users that has its own administrator. This enables the tenant administrators to manage their own resources, security rights and user policies.

There is an overall server system admin which can create and manage organizations and allocate different server resources according to the organizations. The admin in an organization can create and manage users within the organization, assign resource permissions to them, and configure Logi Report Server for the organization. Each organization has its own public resources which can only be accessed by the users within the organization. The organization’s public resources are located in the Organization Reports and Organization Components folders.

This is a separately licensed feature of Logi Report Server. It is installed together with Logi Report Server so only the license key needs to be updated to enable it to work.

![Multi-tenancy](https://devnet.logianalytics.com/hc/article_attachments/9923082069527)
