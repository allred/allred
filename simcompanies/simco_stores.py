#!/usr/bin/env python

# get these values from the Encyclopedia
stores = [
        {
            "name": "car_dealership",
            "kinds": [
                {
                    "name": "economy_car",
                    "kind": 55,
                    "units_sold_per_hour": 1.63,
                    "revenue_less_wages_per_unit": 2271.38,
                    },
                {
                    "name": "economy_e_car",
                    "kind": 53,
                    "units_sold_per_hour": 1.30,
                    "revenue_less_wages_per_unit": 3393.78,
                    },
                {
                    "name": "truck",
                    "kind": 57,
                    "units_sold_per_hour": 0.66,
                    "revenue_less_wages_per_unit": 5696.20,
                    },
                ],
            },
        {
            "name": "gas",
            "kinds": [
                {
                    "name": "petrol",
                    "kind": 11,
                    "units_sold_per_hour": 82.42,
                    "revenue_less_wages_per_unit": 41.10,
                    },
                {
                    "name": "diesel",
                    "kind": 12,
                    "units_sold_per_hour": 79.52,
                    "revenue_less_wages_per_unit": 40.83,
                    },
                ],
            },
        {
            "name": "electronics",
            "kinds": [
                {
                    "name": "smart_phones",
                    "kind": 24,
                    "units_sold_per_hour": 1.57,
                    "revenue_less_wages_per_unit": 650.11,
                    },
                {
                    "name": "tablets",
                    "kind": 25,
                    "units_sold_per_hour": .56,
                    "revenue_less_wages_per_unit": 836.65,
                    },
                {
                    "name": "laptops",
                    "kind": 26,
                    "units_sold_per_hour": .78,
                    "revenue_less_wages_per_unit": 1256.95,
                    },
                {
                    "name": "monitors",
                    "kind": 27,
                    "units_sold_per_hour": 1.28,
                    "revenue_less_wages_per_unit": 574.46,
                    },
                {
                    "name": "tvs",
                    "kind": 28,
                    "units_sold_per_hour": 1.37,
                    "revenue_less_wages_per_unit": 953.78,
                    },
                {
                    "name": "quadcopter",
                    "kind": 98,
                    "units_sold_per_hour": .7,
                    "revenue_less_wages_per_unit": 937.64,
                    },
                ],
            },
        {
                "name": "fashion",
                "kinds": [
                    {
                        "name": "underwear",
                        "kind": 60,
                        "units_sold_per_hour": 23.00,
                        "revenue_less_wages_per_unit": 8.03,
                        },
                    {
                        "name": "gloves",
                        "kind": 61,
                        "units_sold_per_hour": 16.90,
                        "revenue_less_wages_per_unit": 16.10,
                        },
                    {
                        "name": "dress",
                        "kind": 62,
                        "units_sold_per_hour": 40.12,
                        "revenue_less_wages_per_unit": 19.16,
                        },
                    {
                        "name": "heels",
                        "kind": 63,
                        "units_sold_per_hour": 25.74,
                        "revenue_less_wages_per_unit": 22.53,
                        },
                    {
                        "name": "handbags",
                        "kind": 64,
                        "units_sold_per_hour": 15.52,
                        "revenue_less_wages_per_unit": 28.38,
                        },
                    {
                        "name": "sneakers",
                        "kind": 65,
                        "units_sold_per_hour": 26.08,
                        "revenue_less_wages_per_unit": 16.81,
                        },
                    {
                        "name": "lux_watch",
                        "kind": 70,
                        "units_sold_per_hour": 2.33,
                        "revenue_less_wages_per_unit": 757.96,
                        },
                    {
                        "name": "necklace",
                        "kind": 71,
                        "units_sold_per_hour": 1.28,
                        "revenue_less_wages_per_unit": 1497.97,
                        },
                    ],
                },
    {
            "name": "hardware",
            "kinds": [
                {
                    "name": "bricks",
                    "kind": 102,
                    "units_sold_per_hour": 75.85,
                    "revenue_less_wages_per_unit": 3.50,
                    },
                {
                    "name": "cement",
                    "kind": 103,
                    "units_sold_per_hour": 55.22,
                    "revenue_less_wages_per_unit": 7.35,
                    },
                {
                    "name": "planks",
                    "kind": 108,
                    "units_sold_per_hour": 99.09,
                    "revenue_less_wages_per_unit": 10.04,
                    },
                ],
            },
    {
            "name": "grocery",
            "kinds": [
                {
                    "name": "apples",
                    "kind": 3,
                    "units_sold_per_hour": 85.84,
                    "revenue_less_wages_per_unit": 2.18,
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
