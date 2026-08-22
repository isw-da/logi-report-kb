---
title: "Composer Trusted Access Credentials"
id: 47773160502797
section: "Creating and Updating Catalogs Using Catalog Studio Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/47773160502797-Composer-Trusted-Access-Credentials
updated_at: 2026-07-30T20:36:07Z
source_host: logi-report-v26.insightsoftware.com
---
# Configuring Composer Trusted Access Credentials on Server

The Composer Trusted Access Client ID and Client Secret are a system-level configuration that is shared by every Composer import in Catalog Studio, connection refresh, Composer Source import, and Server Console Composer User or Group import. Server administrators configure them once through a properties file. The credentials are no longer requested in the Catalog Studio user interface, the Server Console user interface, or the Import Composer API request body.

Server administrators configure the credentials as follows:

- On the Logi Report Server host, create the file <reporthome>/bin/composer-client.properties if it does not exist.

- Add the following two properties. Use the Trusted Access client that the Composer administrator provisioned for Logi Report Server.
			
- composer.client.id=<trusted-access-client-id>

- composer.client.secret=<trusted-access-client-secret>

- Restrict operating-system access to the file so that only the Logi Report Server service account can read it. Do not commit a populated file to source control.

- Restart Logi Report Server. Server reads the file once at startup, validates that both properties are present and non-blank, and holds the values in memory for the lifetime of the process.

- On the first successful load, Server automatically encrypts the plaintext secret and rewrites the file so that the on-disk copy contains only the encrypted property composer.client.nsecret. From this point onward the file no longer contains a readable secret.

If the file is missing, unreadable, malformed, or either property is blank, every Composer BEARER operation fails fast with an actionable error, and the error message does not contain credential values. Composer BASIC authentication is independent of this file. Changes to the file take effect on the next Server restart.

### Enabling Import From Composer in a Catalog Studio Profile

Server administrators can enable the import entry for a Catalog Studio profile as follows:

- On the Server Console, navigate to Administration > Server Profile > Customize Profile > Catalog Studio.

- Create a profile or edit an existing profile.

- In the Features table, select Visible for Import From Composer.

- Select OK, and make sure the user selects or is assigned a profile in which the feature is visible.

## Importing a Composer Source in Catalog Studio

### Opening the Import Page

- Create a catalog or open an existing catalog in Catalog Studio.

- In the Available Data Sources section, select Import from Composer.

Server displays the Import from Composer page.

### Import Page Options

Specify the options on the Import from Composer page. Fields marked as required must have a value before you can start the import.

| Option | Required | Description |
| --- | --- | --- |
| Data Source | Yes | Select New Data Source to create a data source for the imported resources, or Existing Data Source to add the generated connections, queries, Business Views, and related resources to a data source that already exists in the open catalog. |
| Existing Data Source | Conditional | When you select Existing Data Source, select the target Logi Report data source. The name must match an existing data source in the open catalog. |
| Server URL | Yes | Specify the base URL of the Composer server, including the Composer context path when required, for example, https://composer.example.com/composer. Logi Report Server must be able to access this URL. |
| Username | Yes | Specify the Composer user whose permissions Server uses to retrieve the Source. The user must have access to the selected Source in the specified tenant. The Composer Trusted Access Client ID and Client Secret are read from the Server-side properties file described in Configuring Composer Trusted Access Credentials on Server; the user interface no longer asks for them. |
| Tenant | Conditional | Specify the Composer account name or external tenant ID. This value identifies the account in which Server authenticates the user and retrieves Sources. It is required when the Composer deployment requires an explicit account. |
| Sources | Yes | Select the Composer Source to import. After you provide the connection and authentication information, select Refresh to retrieve the Sources available to the user. A green check mark indicates that Server retrieved and validated the selected Source. |
| Connection Setting | Conditional | Lists the database connections referenced by the selected Source. Select each connection and provide valid target connection values when the values from Composer cannot be used directly in Logi Report. |
| URL | Conditional | Specify the JDBC URL that Logi Report Server uses to access the database. The URL format is defined by the JDBC driver. |
| Username under Connection Setting | Conditional | Specify the database user for the JDBC connection. |
| Password under Connection Setting | Conditional | Specify the database password. The value is masked in the user interface. |
| Test Connection | No | Tests the JDBC URL and credentials before import. Testing every overridden connection is recommended. |
| Qualifier | No | Expands the standard JDBC qualifier settings, including name qualification, quoting, and the database catalog to apply to resources. |
| Data Format | No | Expands the standard JDBC formats for Boolean, Date, Time, and Timestamp values. |
| Transaction | No | Expands the JDBC read-only and transaction isolation settings. |
| Schema | No | Expands the schema selection and the resource types to which the selected schema applies. |
| Conflict Resolution | No | Determines how Server handles a Composer connection that resolves to an existing connection in the target data source when you import into Existing Data Source. Select Create new to always create a new connection (the default), Replace existing to update the matched connection while preserving its Logi Report resource name, or Skip to reuse the matched connection without any changes. New data source imports always create new connections regardless of this option. |
| Import Security Setting | No | Imports column-level security (CLS) for fields and custom metrics, and record-level security (RLS) that Composer models as forced filters, into the target Business View. Cleared by default. When the option is cleared and the selected Source contains any security setting, Server stops the import with an actionable error rather than silently dropping the security metadata. Turn the option on to translate the security definitions into the equivalent Logi Report Business View security. |

The options under Qualifier, Data Format, Transaction, and Schema are the same as the corresponding options for a JDBC connection in Catalog Studio. For descriptions of all advanced settings, see JDBC Connection Properties under Catalog Resource Properties.

### Choosing the Target Data Source

Choose one of the following options:

- 
New Data Source: Server creates a data source and places the generated connection, query, Business View, and related objects in it. The Import Result dialog displays the generated data source name as the target.

- 
Existing Data Source: Server reuses the selected data source and adds the generated resources to it. If the selected data source does not exist or cannot be accessed, the audit result reports an error and does not silently create another data source.

### Configuring Source Connections

After you select a Source, Server lists each connection that the Source references under Connection Setting.

- Select a connection in the list.

- Verify or replace its JDBC URL, database username, and database password.

- Expand Qualifier, Data Format, Transaction, or Schema and modify the advanced JDBC settings when required by the target database.

- Select Test Connection.

- Repeat these steps for every connection in the Source.

The connection selection values identify which Composer connection to override; they do not rename the source connection. Only the connection properties that you explicitly provide are replaced.

### Running the Import and Reviewing the Audit

- After you verify the Source and all connection settings, select Import.

- Wait for Server to translate the Source and create the catalog resources.

- 
Review the Import Result dialog.

The dialog contains the following information:

| Area | Description |
| --- | --- |
| Import status | Indicates whether the import succeeded, completed with issues, or failed. |
| Path | Identifies the catalog that received the imported resources. |
| Target | Identifies the newly created or reused Logi Report data source. |
| Started At and Duration | Show when the import started and how long it took. |
| Imported Object Summary | Shows the total number of audit items and the counts for Success, Errors, Warnings, Unsupported, and Manual Action. |
| Sources | Filters the detail list by imported Source when the result contains more than one Source. |
| Detail | Groups the result items by severity. Expand an item to review its object type, message, diagnostic information, and suggested action. |
| Download > JSON | Downloads the complete machine-readable audit result for automation, diagnostics, or archiving. |
| Download > HTML | Downloads a human-readable audit report for local review or sharing. |
| Auto Download | Automatically downloads the selected audit report when the import completes. |
| Rollback | Reverts the resources created by this import in the current Catalog Studio session. Use it when the audit contains errors that should be corrected before retrying. |
| OK | Accepts the current import result and closes the dialog. |

Use the following guidelines when evaluating the result:

- An import with no errors or manual actions has completed its main translation flow successfully.

- Review every warning. A warning can indicate that Server used a compatible fallback, such as translating an expression to a formula or changing a Business View element type.

- Review every unsupported item to understand which Composer capability was not translated.

- Complete each suggested manual action before using the Business View in production.

- If the result is acceptable, select OK, verify the imported Business View in Catalog Studio, and save the catalog. Import changes are not durable until you save the catalog.

## Calling the Import Composer API

Use catalog.ImportComposer to import a Composer Source programmatically. This section describes only the POST request with an application/json body. Do not place the RPC arguments in the URL query string.

### Endpoint

POST /studio/rpc/catalog.importComposer

The endpoint route uses catalog.importComposer; the function in the JSON body uses the exact case catalog.ImportComposer.

### Request Headers

| Header | Required | Value and description |
| --- | --- | --- |
| Authorization | Yes | Bearer . The token authorizes access to the Logi Report API. |
| Content-Type | Yes | application/json. |
| Accept | No | application/json. |

The Logi Report access token in the Authorization header is separate from the Composer credentials in the request body.

### JSON Body Structure

{

  "func": "catalog.ImportComposer",

  "args": {

    "serverUrl": "https://composer.example.com/composer",

    "authType": "BEARER",

    "sourceIds": ["<composer-source-id>"],

    "username": "<composer-user>",

    "account": "<composer-account>"

  }

}

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| func | String | Yes | RPC function name. Specify catalog.ImportComposer. |
| args | Object | Yes | Contains the import arguments described in the following table. |

The request body no longer accepts clientId or clientSecret. Server reads the Composer Trusted Access Client ID and Client Secret from the Server-side properties file described in Configuring Composer Trusted Access Credentials on Server. Legacy request bodies that still supply these fields are tolerated for transition compatibility but are ignored.

### Import Arguments

| Argument | Type | Required | Description |
| --- | --- | --- | --- |
| serverUrl | String | Yes | Composer Server base URL, for example, https://composer.example.com/composer. |
| sourceIds | Array of strings | Yes | Composer Source IDs to import. Specify at least one Source ID. |
| username | String | Yes | Composer username. In BEARER mode, this is the target user for Trusted Access authentication. |
| account | String | Conditional | Composer account name or external tenant ID. In BEARER mode, Server uses this value to identify the tenant for the Trusted Access request. Specify it when the Composer deployment requires an explicit account. |
| datasource | String | No | Name of an existing Logi Report data source. When present, Server adds the generated resources to this data source. When omitted, Server creates a data source. |
| connections | Array of objects | No | Overrides properties of connections retrieved with the Source. Server matches an override by connectionId, then by name; it uses url as the selector only when both are absent. The selector does not rename the matched connection. |
| catalog | Object | No | Catalog definition, for example, {"name":"//.cat"}. If no catalog is currently open, Server opens this catalog before importing. If a catalog is already open, Server uses the open catalog. |
| options | Object | No | Optional import behavior overrides. See Import Options. |

### Import Options

Set the options object to control import behaviors that also appear in the Catalog Studio user interface. All properties are optional.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| importStrategy | String | No | Handling of Composer connections whose Composer connection ID matches an existing connection in the target data source when you import into an existing data source. Supported lowercase values are new, replace, and skip. The default is new. New data source imports always use new regardless of the value supplied here. |
| importSecurity | Boolean | No | Whether to import Composer security settings into the target Business View. When true, Server translates Composer column-level security (CLS) for fields and custom metrics and record-level security (RLS) from forced filters into equivalent Logi Report Business View security. When false (the default) and the selected Source contains any security setting, Server stops the import with an actionable error instead of silently dropping the security metadata. |

### Connection Override Properties

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| connectionId | String | No | Composer connection ID used as the preferred match selector. |
| name | String | No | Composer connection name used when connectionId is absent. |
| url | String | No | Replacement JDBC URL. It is also the fallback selector only when connectionId and name are absent. |
| user | String | No | Replacement database username. |
| password | String | No | Replacement database password. Treat this value as sensitive. |

Only explicitly provided, non-empty override values replace values retrieved from Composer. The connectionId and name properties select a connection and are not used to rename it.

### Example: Creating a Data Source

The following request omits datasource, so Server creates a data source in the currently open catalog.

POST https://report.example.com/studio/rpc/catalog.importComposer HTTP/1.1

Authorization: Bearer <logi-report-access-token>

Content-Type: application/json

Accept: application/json

{

  "func": "catalog.ImportComposer",

  "args": {

    "serverUrl": "https://composer.example.com/composer",

    "sourceIds": ["<composer-source-id>"],

    "username": "<composer-user>",

    "account": "<composer-account>",

    "connections": [

      {

        "name": "<composer-connection-name>",

        "url": "jdbc:postgresql://db.example.com:5432/<database>",

        "user": "<database-user>",

        "password": "<database-password>"

      }

    ]

  }

}

### Example: Reusing an Existing Data Source

To add imported resources to an existing data source, include datasource in args.

POST https://report.example.com/studio/rpc/catalog.importComposer HTTP/1.1

Authorization: Bearer <logi-report-access-token>

Content-Type: application/json

Accept: application/json

{

  "func": "catalog.ImportComposer",

  "args": {

    "serverUrl": "https://composer.example.com/composer",

    "sourceIds": ["<composer-source-id>"],

    "username": "<composer-user>",

    "account": "<composer-account>",

    "datasource": "<existing-logi-report-data-source>",

    "connections": [

      {

        "connectionId": "<composer-connection-id>",

        "url": "jdbc:postgresql://db.example.com:5432/<database>",

        "user": "<database-user>",

        "password": "<database-password>"

      }

    ]

  }

}

If no catalog is already open, add the following object to args:

"catalog": {

  "name": "/<folder>/<catalog-name>.cat"

}

### Successful Response

A successful RPC call returns err as 0. The audit counts determine whether all individual resources were translated successfully.

{

  "err": 0,

  "action": "catalog.ImportComposer",

  "result": {

    "datasource": "<target-data-source>",

    "successCount": 12,

    "errorCount": 0,

    "warningCount": 1,

    "totalCount": 13,

    "audit": {

      "requestId": "<import-request-id>",

      "sourceType": "composer",

      "sourceId": "<composer-source-id>",

      "startedAt": 1784959200000,

      "endedAt": 1784959202400,

      "durationMs": 2400,

      "totalCount": 13,

      "successCount": 12,

      "warningCount": 1,

      "errorCount": 0,

      "unsupportedCount": 0,

      "manualActionCount": 0,

      "items": []

    },

    "translations": []

  }

}

| Response property | Description |
| --- | --- |
| err | RPC status. 0 means Server accepted and executed the RPC call. A value other than 0 indicates an RPC-level failure. |
| result.datasource | Data source created or reused by the import. |
| result.successCount | Number of successful audit items. |
| result.warningCount | Number of items translated with a warning. |
| result.errorCount | Number of failed audit items. Do not treat the import as fully successful when this value is greater than 0. |
| result.totalCount | Total number of audit items. |
| result.audit | Detailed import audit. |
| result.translations | Source-to-catalog translation summaries. |

The audit object contains timing and correlation information as well as these result counts:

| Audit property | Description |
| --- | --- |
| requestId | Import request ID. Use it to correlate the result with Server logs. |
| unsupportedCount | Number of Composer capabilities that the current translator could not convert automatically. |
| manualActionCount | Number of items that require follow-up action. |
| items | Detailed results for imported objects. Each item can contain phase, severity, category, itemType, itemId, itemName, code, message, detail, suggestedAction, requiresManualAction, and context. |

Evaluate both the outer err value and the audit counts:

| Condition | Meaning | Action |
| --- | --- | --- |
| err = 0, errorCount = 0, and manualActionCount = 0 | The main import flow succeeded. | Review warnings, then save the catalog. |
| warningCount > 0 | The import completed with compatible fallbacks or diagnostics. | Review all warning items before saving. |
| unsupportedCount > 0 | Some Composer capabilities were not translated. | Review the affected objects and decide whether to model them manually. |
| manualActionCount > 0 | Follow-up work is required. | Follow each item's suggestedAction. |
| errorCount > 0 | At least one object failed to import. | Correct the problem or roll back before saving. |
| err is not 0 | The RPC request failed. | Check the Report token, permissions, catalog state, and JSON format. |
