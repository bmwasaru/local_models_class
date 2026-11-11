#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to get the current date in Africa/Nairobi timezone.
This script uses the 'dateutil' library which is compatible with the
Python 2 and 3 environments.
"""

from datetime import datetime
from dateutil import parser


def main():
    # Get current time in Nairobi timezone (Africa/Nairobi)
    try:
        print("Current Date & Time in Africa/Nairobi:")
        now = parser.parse(datetime.now(timezoneinfo="Africa/Nairobi"))
        print(now.strftime("%A, %B %d, %Y at %I:%M %p"))
    except Exception as e:
        print(f"Error getting time in Nairobi timezone: {e}")


if __name__ == "__main__":
    main()
