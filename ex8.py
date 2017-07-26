# -*- coding: utf-8 -*-
formatter = "%s %s %s %s"

print formatter %(1, 2, 3, 4)
print formatter %("一", "二", "三","四")
print formatter %(True, False, False, True)
print formatter %(formatter, formatter, formatter, formatter)
print formatter %(
    "I had this thing.",
    "That you could type up right.",
    "But it did't sing.",
    "So I said goodnight."
)