---
title: "Configuring the Email Server"
id: 45203882268941
section: "Configuring Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203882268941-Configuring-the-Email-Server
updated_at: 2026-04-30T14:08:03Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Configuring the Email Server

In order for users to publish reports to email and to notify the task status via email when scheduling tasks to run reports, create in-memory cubes, or create CRDs, administrators need to configure an email server in advance. This topic describes how you can configure an email server on the Server Console.

- On the system toolbar of the Server Console, navigate to Administration > Configuration > E-mail Server. Server displays the E-mail Server page.
    

- In the SMTP Server text box, type the numeric or named host of the machine where the email server is.

- In the SMTP Server Port text box, type the port where the email server runs.

- If the SMTP server requires authentication, select Server Requires Authentication, then specify 
 the username and password for signing in to the SMTP server.

- If the SMTP server requires a secure connection, select Server Requires a Secure Connection (SSL) or Server Requires a Secure Connection (STARTTLS) according to the SMTP server configuration. 

- In the E-mail Address text box, type the address of the email sender. Make sure that the format of the specified address is valid.

- From the Encoding list, select the encoding for the titles and comments of the email.

- Select Save to apply the settings.

Server saves the email server settings in the mailconfig.properties file in the <install_root>\bin directory. You can also use the property file for default email server configuration. The following table lists the available properties in the property file and the UI options they map to.

| Property in mailconfig.properties | Mapped UI Option |
| --- | --- |
| smtp.server | SMTP Server |
| smtp.server.port | SMTP Server Port |
| smtp.authentication | Server Requires Authentication |
| smtp.SSL | Server Requires a Secure Connection (SSL) |
| smtp.TLS | Server Requires a Secure Connection (STARTTLS) |
| mailbox | E-mail Address |
| mail.encoding | Encoding |
| smtp.user | SMTP Login Account > User Name |
| smtp.npassword | SMTP Login Account > Password |

### Configuring OAuth 2.0 (Authorization Code) for Email Server

Follow these steps to configure the OAuth 2.0 (Authorization Code) authentication method for your email server. This setup is suitable for integrations with modern identity providers like Microsoft (Office 365).

#### 1. Configure the OAuth Provider

First, define the OAuth provider details on the server.

- Navigate to the <Server_Home>/bin directory.

- Locate or create the file mail_oauth_providers.json.

- 

Add the following JSON content to the file. Customize the clientId, tenantId, and redirectUri fields as needed.

Example: Microsoft Office 365 Configuration

{

  "providers": [

    {

      "name": "Microsoft",

      "displayName": "Microsoft (Office 365)",

      "providerClass": "jet.server.api.admin.cfg.MicrosoftOAuthProvider",

      "authorizedUri": "https://login.microsoftonline.com/{tenantId}/oauth2/v2.0/authorize",

      "tokenEndpoint": "https://login.microsoftonline.com/{tenantId}/oauth2/v2.0/token",

      "clientId": "your-microsoft-client-id",

      "tenantId": "your-microsoft-tenant-id",

      "scope": "https://outlook.office.com/SMTP.Send offline_access",

      "redirectUri": "http://{your-server-address}/admin/config/oauth_callback.jsp",

      "props": {

        "prompt": "consent",

        "access_type": "offline"

      }

    }

  ]

}

Note: 

- redirectUri: Ensure this URL matches the "Redirect URI (Web)" configured in your Azure AD application registration. Typically, the path is /admin/config/oauth_callback.jsp (adjust the context path according to your deployment).

- providerClass: The example uses the default Microsoft implementation. If you use another provider (e.g., Google), implement the jet.server.api.admin.cfg.OAuthProvider interface and verify the fully qualified class name in this file.

#### 2. Select Authentication Mode in Console

- Log in to the Report Server Console.

- Go to Administration > Configuration > E-mail Server

- In the Authentication Mode drop-down list, select OAuth 2.0 (Authorization Code).

- In the subsequent Provider drop-down list, select the provider configured in step 1 (e.g., "Microsoft (Office 365)").

#### 3. Save and Authorize

After configuring the provider, perform a one-time authorization to generate the refresh token.

- Click Save at the bottom of the page to apply the settings.

- Once saved, locate and click the "Generate Access Token" link/button on the page.
- You will be redirected to the Microsoft login page.

- Sign in with the email account that has permissions to send emails.

- Click "Accept" on the consent prompt.

- Upon successful authorization, the browser will redirect back to the Report Server configuration page. The system will automatically acquire and store the refresh token. You can now test the email configuration.
