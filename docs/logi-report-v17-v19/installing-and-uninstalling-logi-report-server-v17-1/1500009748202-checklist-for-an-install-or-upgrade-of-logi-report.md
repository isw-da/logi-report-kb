---
title: "Checklist for an Install or Upgrade of Logi Report"
id: 1500009748202
section: "Installing and Uninstalling Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009748202-Checklist-for-an-Install-or-Upgrade-of-Logi-Report
updated_at: 2021-07-24T00:48:08Z
---

# Checklist for an Install or Upgrade of Logi Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880314007/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748182-Installing-and-Uninstalling-Logi-Report-Server)  [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880314519/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776661-Logi-Report-Licenses)

# Checklist for an Install or Upgrade of Logi Report

When you install or upgrade Logi Report, you need to prepare your environment first. This topic describes the checklist for an install or an upgrade of Logi Report.

Make sure you meet the minimum system requirements before an install and an upgrade. Select the following links to see the hardware, software, and other system requirements for Logi Report:

* System Requirements in the *Logi Report Designer Guide*
* [System Requirements for Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009776801-Logi-Report-Server-System-Requirements)

This topic contains the following sections:

* [Checklist for an Install](#Install)
* [Checklist for an Upgrade](#Upgrade)

## Checklist for an Install

Make sure you have everything ready before you perform an install of Logi Report.

First, you need to decide the licensed features that you want. Select the following link to see the licensed features in Logi Report: [Logi Report Licenses](https://devnet.logianalytics.com/hc/en-us/articles/1500009776661-Logi-Report-Licenses).

Second, determine the number of servers you need if you want to set up a Logi Report Server Cluster. Make business decisions about how you will be load balancing, and how many persons in your organization will use Logi Report. Select the following link to read up Logi Report best practices: [Logi Report Server Cluster](https://devnet.logianalytics.com/hc/en-us/articles/1500009743402-Logi-Report-Server-Cluster).

Next, you need to obtain the software. Select the following link to get the files you need: [Logi Report download center](https://www.jinfonet.com/product/download-jreport/).

Then, during the install of Logi Report using the Installation Wizard, add the report database driver into the class path. For Logi Report Server, also configure the system database and add the system database driver into the class path. Select the following links to see the various ways and procedures of installing Logi Report:

* Installing and Running Designer in the *Logi Report Designer Guide*
* [Installing and Uninstalling Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009748182-Installing-and-Uninstalling-Logi-Report-Server)
* Installing and Uninstalling Server Monitor in the *Logi Report Server Monitor Guide*

Then, after you have finished installing Logi Report, start Designer and then prepare the reporting environment.

1. Create a new catalog. See Creating, Opening, and Saving Catalogs in the *Logi Report Designer Guide*.
2. Set up data source connection to your report database. See Connecting to Your Data Sources in the *Logi Report Designer Guide*.
3. Create queries and business views for providing data resources to reports. See Creating Queries in a Catalog and Creating Business Views in a Catalog in the *Logi Report Designer Guide*.
4. Create reports and library components. See Creating Reports in the *Logi Report Designer Guide*.
5. Publish your catalogs and reports from Designer to Server. See Publishing and Downloading Resources in the *Logi Report Designer Guide*.

Then, start Server and define your user roles and the permissions on the reports. Select the following links to learn more about user roles and permissions in Logi Report:

* [Security System Data Model](https://devnet.logianalytics.com/hc/en-us/articles/1500009778581-Security-System-Data-Model)
* [Using an LDAP Server's Security System](https://devnet.logianalytics.com/hc/en-us/articles/1500009778661-Using-an-LDAP-Server-s-Security-System)

## Checklist for an Upgrade

You should back up the following resources before you perform an upgrade of Logi Report:

* The reports in Designer
* The reports in the `<install_root>\history` directory in Server
* The server database in Server. Select the following link to see how to back up and restore the server database: [Managing Server Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009748642-Managing-Server-Data).
* The `<install_root>\lib` directory
* The `<install_root>\public_html` directory

Select the following links to see the procedures of upgrading Logi Report:

* Installing Updates/Service Packs in the *Logi Report Designer Guide*
* [Upgrading Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009748302-Upgrading-Logi-Report-Server)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880314007/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748182-Installing-and-Uninstalling-Logi-Report-Server)   [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880314519/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776661-Logi-Report-Licenses)
