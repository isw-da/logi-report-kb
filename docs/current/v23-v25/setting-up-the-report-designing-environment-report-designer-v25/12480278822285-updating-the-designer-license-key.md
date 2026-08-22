---
title: "Updating the Designer License Key"
id: 12480278822285
section: "Setting Up the Report Designing Environment - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480278822285-Updating-the-Designer-License-Key
updated_at: 2026-02-25T23:48:23Z
source_host: docs-report.zendesk.com
---
# Updating the Designer License Key

Report restricts specific features by licenses. You can update your Report Designer key to take advantage of the features in a new release, and you will want to update your key when your current key expires. This topic describes how you can update your license key in the command line without having to reinstall Designer.

- Open a Command Prompt window.

- Open the <install_root>\bin directory of your Designer. 

- Type the command:
                rp UID INSTALLKEY

Where, UID is your user ID and INSTALLKEY is the new key. If your UID contains space, you need to quote it. You can copy the key and paste it to the command window by selecting the command icon on the window title bar and navigating to Edit > Paste.

- Select Enter on the keyboard to confirm the change.
