# Changelog

## [Unreleased]
- Planned: real-time alert notifications
- Planned: user role management

## [1.2.5] - 2026-06-24
- Added user session timeout indicator to dashboard header
- Fixed duplicate alert entries appearing after rapid filter toggling
- Improved metric card rendering performance on low-resolution displays
- Added tooltips to severity badge icons for accessibility

## [1.2.4] - 2026-06-21
- Minor improvements to alert panel rendering stability
- Updated dependency versions for security patches
- Small fixes to metric chart tooltip positioning

## [1.2.3] - 2026-06-18
- Added customizable widget layout drag-and-drop persistence across sessions
- Fixed timezone display mismatch on time-series metric charts
- Improved initial dashboard load time by deferring off-screen widget rendering
- Added severity filter chips to the alerts overview panel

## [1.2.2] - 2026-06-14
- Added per-widget refresh interval configuration in dashboard settings
- Fixed stale data display when switching between metric views
- Improved error boundary handling for failed widget data fetches
- Added keyboard shortcut support for dashboard panel navigation

## [1.2.1] - 2026-06-07
- Minor improvements to alert deduplication logic
- Refactored metric aggregation for lower memory usage
- Updated dependency versions for security patches

## [1.2.0] - 2026-06-04
- Added exportable PDF reports for dashboard snapshots
- Improved widget loading performance with lazy data fetching
- Fixed race condition in concurrent metric refresh calls
- Added dark mode toggle to dashboard settings

## [1.1.0] - 2026-05-28
- Minor UI improvements to dashboard widgets
- Improved data refresh intervals for security metrics

## [1.0.0] - 2026-05-10
- Initial release
- Security dashboard with key metrics overview
- Integration with common security event sources
