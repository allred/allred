#!/usr/bin/env python

# get these values from the Encyclopedia
stores = [
        {
            "name": "sales_office",
            "kinds": [
                {
                    "name": "bfr",
                    "kind": 94,
                    "units_sold_per_hour": 0.21,
                    "revenue_less_wages_per_unit": 2271.38,
                },
            ]
        },
        {
            "name": "car_dealership",
            "kinds": [
                {
                    "name": "economy_e_car",
                    "kind": 53,
                    "units_sold_per_hour": .89,
                    "revenue_less_wages_per_unit": 3196.09,
                    },
                {
                    "name": "luxury_e_car",
                    "kind": 54,
                    "units_sold_per_hour": 0.29,
                    "revenue_less_wages_per_unit": 6080.93,
                    },
                {
                    "name": "economy_car",
                    "kind": 55,
                    "units_sold_per_hour": 1.18,
                    "revenue_less_wages_per_unit": 2155.41,
                    },
                {
                    "name": "luxury_car",
                    "kind": 56,
                    "units_sold_per_hour": 0.31,
                    "revenue_less_wages_per_unit": 4075.47,
                    },
                {
                    "name": "truck",
                    "kind": 57,
                    "units_sold_per_hour": 0.47,
                    "revenue_less_wages_per_unit": 5412.58,
                    },
                ],
            },
        {
            "name": "gas",
            "kinds": [
                {
                    "name": "petrol",
                    "kind": 11,
                    "units_sold_per_hour": 58.47,
                    "revenue_less_wages_per_unit": 39.09,
                    },
                {
                    "name": "diesel",
                    "kind": 12,
                    "units_sold_per_hour": 57.48,
                    "revenue_less_wages_per_unit": 38.74,
                    },
                ],
            },
        {
            "name": "electronics",
            "kinds": [
                {
                    "name": "smart_phones",
                    "kind": 24,
                    "units_sold_per_hour": 1.37,
                    "revenue_less_wages_per_unit": 626.07,
                    },
                {
                    "name": "tablets",
                    "kind": 25,
                    "units_sold_per_hour": .49,
                    "revenue_less_wages_per_unit": 798.48,
                    },
                {
                    "name": "laptops",
                    "kind": 26,
                    "units_sold_per_hour": .60,
                    "revenue_less_wages_per_unit": 1176.75,
                    },
                {
                    "name": "monitors",
                    "kind": 27,
                    "units_sold_per_hour": 1.16,
                    "revenue_less_wages_per_unit": 541.83,
                    },
                {
                    "name": "tvs",
                    "kind": 28,
                    "units_sold_per_hour": 1.18,
                    "revenue_less_wages_per_unit": 924.19,
                    },
                {
                    "name": "quadcopter",
                    "kind": 98,
                    "units_sold_per_hour": .63,
                    "revenue_less_wages_per_unit": 892.78,
                    },
                ],
            },
        {
                "name": "fashion",
                "kinds": [
                    {
                        "name": "underwear",
                        "kind": 60,
                        "units_sold_per_hour": 24.53,
                        "revenue_less_wages_per_unit": 7.89,
                        },
                    {
                        "name": "gloves",
                        "kind": 61,
                        "units_sold_per_hour": 17.03,
                        "revenue_less_wages_per_unit": 15.20,
                        },
                    {
                        "name": "dress",
                        "kind": 62,
                        "units_sold_per_hour": 36.65,
                        "revenue_less_wages_per_unit": 19.02,
                        },
                    {
                        "name": "heels",
                        "kind": 63,
                        "units_sold_per_hour": 24.83,
                        "revenue_less_wages_per_unit": 22.01,
                        },
                    {
                        "name": "handbags",
                        "kind": 64,
                        "units_sold_per_hour": 14.23,
                        "revenue_less_wages_per_unit": 26.15,
                        },
                    {
                        "name": "sneakers",
                        "kind": 65,
                        "units_sold_per_hour": 22.69,
                        "revenue_less_wages_per_unit": 15.60,
                        },
                    {
                        "name": "lux_watch",
                        "kind": 70,
                        "units_sold_per_hour": 1.77,
                        "revenue_less_wages_per_unit": 707.90,
                        },
                    {
                        "name": "necklace",
                        "kind": 71,
                        "units_sold_per_hour": 1.00,
                        "revenue_less_wages_per_unit": 1401.01,
                        },
                    ],
                },
    {
            "name": "hardware",
            "kinds": [
                {
                    "name": "bricks",
                    "kind": 102,
                    "units_sold_per_hour": 74.74,
                    "revenue_less_wages_per_unit": 3.44,
                    },
                {
                    "name": "cement",
                    "kind": 103,
                    "units_sold_per_hour": 50.87,
                    "revenue_less_wages_per_unit": 7.11,
                    },
                {
                    "name": "planks",
                    "kind": 108,
                    "units_sold_per_hour": 82.82,
                    "revenue_less_wages_per_unit": 9.48,
                    },
                {
                    "name": "windows",
                    "kind": 109,
                    "units_sold_per_hour": 11.84,
                    "revenue_less_wages_per_unit": 98.19,
                    },
                {
                    "name": "tools",
                    "kind": 110,
                    "units_sold_per_hour": 10.16,
                    "revenue_less_wages_per_unit": 176.74,
                    },
                ],
            },
    {
            "name": "grocery",
            "kinds": [
                {
                    "name": "apples",
                    "kind": 3,
                    "units_sold_per_hour": 83.45,
                    "revenue_less_wages_per_unit": 2.10,
                    },
                {
                    "name": "oranges",
                    "kind": 4,
                    "units_sold_per_hour": 63.42,
                    "revenue_less_wages_per_unit": 2.24,
                    },
                {
                    "name": "grapes",
                    "kind": 5,
                    "units_sold_per_hour": 63.19,
                    "revenue_less_wages_per_unit": 2.73,
                    },
                {
                    "name": "steak",
                    "kind": 7,
                    "units_sold_per_hour": 20.76,
                    "revenue_less_wages_per_unit": 11.76,
                    },
                {
                    "name": "eggs",
                    "kind": 9,
                    "units_sold_per_hour": 290.79,
                    "revenue_less_wages_per_unit": 1.21,
                    },
                {
                    "name": "sausages",
                    "kind": 8,
                    "units_sold_per_hour": 80.41,
                    "revenue_less_wages_per_unit": 3.90,
                    },
                ],
            },
    ]
