# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [2.3.6] - 2024-05-10

### Added

- When `environments` property is set on the `context` the global `environment` value is overwriten.

## [2.3.7] - 2024-06-30

### Added

- Added support for the Feedback API
- Introduce the `BASE_URL` environment variable to prepare the SDK for on premise deployments

### Changed

- Centralize the `api_key` in the `Store` object to reuse it in all the API calls
