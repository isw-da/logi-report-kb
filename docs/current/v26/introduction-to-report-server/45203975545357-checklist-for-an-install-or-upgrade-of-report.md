---
title: "Checklist for an Install or Upgrade of Report"
id: 45203975545357
section: "Introduction to Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203975545357-Checklist-for-an-Install-or-Upgrade-of-Report
updated_at: 2026-04-30T14:10:12Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Checklist for an Install or Upgrade of Report

When you install or upgrade Report, you need to prepare your environment first. This topic describes the checklist for an install or an upgrade of Report.

Make sure you meet the minimum system requirements before an install and an upgrade. Select the following links to see the hardware, software, and other system requirements for Report:

- 
System Requirements in the Report Designer Guide

- System Requirements for Report Server

This topic contains the following sections:

- Checklist for an Install

- Checklist for an Upgrade

## 
Checklist for an Install

Make sure you have everything ready before you perform an install of Report.

First, you need to decide the licensed features that you want. Select the following link to see the licensed features in Report: Report Licenses.

Second, determine the number of servers you need if you want to set up a Report Server Cluster. Make business decisions about how you will be load balancing, and how many persons in your organization will use Report. Select the following link to read up Report best practices: Report Server Cluster. 

Next, you need to obtain the software. Select the following link to get the files you need: Report download center.

Then, during the install of Report using the Installation Wizard, add the report database driver into the class path. For Report Server, also configure the system database and add the system database driver into the class path. Select the following links to see the various ways and procedures of installing Report:

- 
Installing and Running Designer in the Report Designer Guide

- Installing and Uninstalling Report Server

- 
Installing and Uninstalling Server Monitor in the Report Server Monitor Guide

Then, after you have finished installing Report, start Designer and then prepare the reporting environment. 

- Create a new catalog. See Creating, Opening, and Saving Catalogs in the Report Designer Guide.

- Set up data source connection to your report database. See Connecting to Your Data Sources in the Report Designer Guide.

- Create queries and business views for providing data resources to reports. See Creating Queries in a Catalog and Creating Business Views in a Catalog in the Report Designer Guide.

- Create reports and library components. See Creating Reports in the Report Designer Guide.

- Publish your catalogs and reports from Designer to Server. See Publishing and Downloading Resources in the Report Designer Guide.

Then, start Server and define your user roles and the permissions on the reports. Select the following links to learn more about user roles and permissions in Report: 

- Security System Data Model

- Using an LDAP Server's Security System

## 
Checklist for an Upgrade

You should back up the following resources before you perform an upgrade of Report:

- The reports in Designer

- The reports in the <install_root>\history directory in Server

- The server database in Server. Select the following link to see how to back up and restore the server database: Managing Server Data.

- The <install_root>\lib directory

- The <install_root>\public_html directory

Select the following links to see the procedures of upgrading Report:

- 
Installing Service Packs in the Report Designer Guide

- Upgrading Report Server
