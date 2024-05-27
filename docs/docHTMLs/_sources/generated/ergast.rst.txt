.. _ergast:

Ergast API Interface
====================

.. currentmodule::
  fastf1.ergast

Introduction
------------

This module can be used to interface with the Ergast F1 API
(https://ergast.com/mrd/). All Ergast endpoints are supported.

The :class:`Ergast` object provides access to all API Endpoints of the
Ergast API.

The terms of use of Ergast apply (https://ergast.com/mrd/terms/).
Especially take care not to exceed the specified rate limits.
FastF1 will handle caching and it will try to enforce rate limits where
possible. Make sure to know what limits apply. For more information on how
FastF1 handles caching and rate limiting see :ref:`requests-and-caching`.
