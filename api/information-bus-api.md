# Information Bus API

The Information Bus carries information around inside Logi Report Server. You get a bus
instance, get or put values into a container, and choose how long each value survives.

Primary source: [Information Bus API (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741386457495-information-bus-api.md).
Era: `logi-report-v17-v19`.

## The four interfaces

- **InformationBus** transmits information in the server. It holds three kinds of
  container, at global level, organisation level and user level, and you get or put
  information in them.
- **InformationBusManager** returns the Information Bus instance.
- **InformationContainer** stores user information under one of three life cycles.
- **InfoLifeCycleType** names that life cycle.

## Life cycles

| Value | Behaviour |
| --- | --- |
| `LONG_TIME` | Stays until removed, or until its container is removed |
| `SPECIFIED_TIME` | Stays until the time you specify, or until removed, or until its container is removed |
| `ONCE_TIME` | Removed as soon as you get it or remove it, or when its container is removed |

## When to reach for it

Three-level scoping (global, organisation, user) makes it the documented route for passing
state between server-side components in a multi-tenant setup, rather than parking state in
a servlet session. That is what the corpus supports; it does not give a worked example, a
method signature, or a package name for these interfaces, so do not invent one. Check the
Javadoc on an install for the package.

## Era note

The same four-interface description appears across all three trees:
[v15, Logi JReport](../docs/jreport-v15-v16/working-with-apis-logi-jreport-server-v15/1500009668661-information-bus-api.md),
[unversioned](../docs/unversioned/using-the-server-api/1500009712041-information-bus-api.md),
and v19. No change is documented across the rename.
