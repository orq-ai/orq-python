# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [2.13.3] - 2024-09-19

### Fixed

- Missing invoke_options parameter

## [2.13.2] - 2024-09-17

### Added

- Now is possible to request the retrieval to be returned in the response of the deployment creation

## [2.13.1] - 2024-09-17

### Fixed

- Incorrect URL for the async methods of the Deployments API

## [2.13.0] - 2024-08-03

### Added

- Added support for webhooks signature verification
- Added support for the `contacts` API

## [2.12.0] - 2024-07-09

### Added

- Added support for `prefix_messages` in deployments

## [2.11.0] - 2024-06-30

### Added

- Added support for the Feedback API
- Introduce the `BASE_URL` environment variable to prepare the SDK for on premise deployments

### Changed

- Centralize the `api_key` in the `Store` object to reuse it in all the API calls

## [2.3.6] - 2024-05-10

### Added

- When `environments` property is set on the `context` the global `environment` value is overwriten.
