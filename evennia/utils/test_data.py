from anything import Something
from random import randint

olc_menus_obj_diff = {
            "attrs": {
                "desc": (
                    ("desc", "This is User #1.", None, ""),
                    ("desc", "This is User #1.", None, ""),
                    "KEEP",
                ),
                "foo": (None, ("foo", "bar", None, ""), "ADD"),
                "prelogout_location": (
                    ("prelogout_location", "#2", None, ""),
                    ("prelogout_location", "#2", None, ""),
                    "KEEP",
                ),
            },
            "home": ("#2", "#2", "KEEP"),
            "key": ("TestChar", "TestChar", "KEEP"),
            "locks": (
                (
                    "boot:false();call:false();control:perm(Developer);delete:false();"
                    "edit:false();examine:perm(Developer);get:false();msg:all();"
                    "puppet:false();tell:perm(Admin);view:all()"
                ),
                (
                    "boot:false();call:false();control:perm(Developer);delete:false();"
                    "edit:false();examine:perm(Developer);get:false();msg:all();"
                    "puppet:false();tell:perm(Admin);view:all()"
                ),
                "KEEP",
            ),
            "permissions": {"developer": ("developer", "developer", "KEEP")},
            "prototype_desc": ("Testobject build", None, "REMOVE"),
            "prototype_key": ("TestDiffKey", "TestDiffKey", "KEEP"),
            "prototype_locks": ("spawn:all();edit:all()", "spawn:all();edit:all()", "KEEP"),
            "prototype_tags": {},
            "tags": {"foo": (None, ("foo", None, ""), "ADD")},
            "typeclass": (
                "typeclasses.characters.Character",
                "typeclasses.characters.Character",
                "KEEP",
            ),
        }

olc_menus_obj_diff_expected = "".join(["- |wattrs:|n    |c[1] |yADD|n: foo |W=|n bar |W(category:|n None|W, locks:|n |W)|n",
                                    "\n- |whome:|n",
                                    "\n- |wkey:|n",
                                    "\n- |wlocks:|n",
                                    "\n- |wpermissions:|n",
                                    "\n- |wprototype_desc:|n    |c[2] |rREMOVE|n: Testobject build",
                                    "\n- |wprototype_key:|n",
                                    "\n- |wprototype_locks:|n",
                                    "\n- |wprototype_tags:|n",
                                    "\n- |wtags:|n    |c[3] |yADD|n: foo |W(category:|n None|W)|n",
                                    "\n- |wtypeclass:|n"])

olc_menus_expected_tree = [
        "node_index",
        [
            "node_prototype_key",
            [
                "node_index",
                "node_index",
                "node_index",
                "node_validate_prototype",
                ["node_index", "node_index", "node_index"],
                "node_index",
            ],
            "node_prototype_parent",
            [
                "node_prototype_parent",
                "node_prototype_key",
                "node_prototype_parent",
                "node_index",
                "node_validate_prototype",
                "node_index",
            ],
            "node_typeclass",
            [
                "node_typeclass",
                "node_prototype_parent",
                "node_typeclass",
                "node_index",
                "node_validate_prototype",
                "node_index",
            ],
            "node_key",
            ["node_typeclass", "node_key", "node_index", "node_validate_prototype", "node_index"],
            "node_aliases",
            ["node_key", "node_aliases", "node_index", "node_validate_prototype", "node_index"],
            "node_attrs",
            ["node_aliases", "node_attrs", "node_index", "node_validate_prototype", "node_index"],
            "node_tags",
            ["node_attrs", "node_tags", "node_index", "node_validate_prototype", "node_index"],
            "node_locks",
            ["node_tags", "node_locks", "node_index", "node_validate_prototype", "node_index"],
            "node_permissions",
            [
                "node_locks",
                "node_permissions",
                "node_index",
                "node_validate_prototype",
                "node_index",
            ],
            "node_location",
            [
                "node_permissions",
                "node_location",
                "node_index",
                "node_validate_prototype",
                "node_index",
                "node_index",
            ],
            "node_home",
            [
                "node_location",
                "node_home",
                "node_index",
                "node_validate_prototype",
                "node_index",
                "node_index",
            ],
            "node_destination",
            [
                "node_home",
                "node_destination",
                "node_index",
                "node_validate_prototype",
                "node_index",
                "node_index",
            ],
            "node_prototype_desc",
            [
                "node_prototype_key",
                "node_prototype_parent",
                "node_index",
                "node_validate_prototype",
                "node_index",
            ],
            "node_prototype_tags",
            [
                "node_prototype_desc",
                "node_prototype_tags",
                "node_index",
                "node_validate_prototype",
                "node_index",
            ],
            "node_prototype_locks",
            [
                "node_prototype_tags",
                "node_prototype_locks",
                "node_index",
                "node_validate_prototype",
                "node_index",
            ],
            "node_validate_prototype",
            "node_index",
            "node_prototype_spawn",
            ["node_index", "node_index", "node_validate_prototype"],
            "node_index",
            "node_search_object",
            ["node_index", "node_index", "node_index"],
        ],
    ]

expected_spawned_prototype = {
                "attrs": [("test", "testval", None, "")],
                "home": Something,
                "key": "Obj",
                "location": Something,
                "locks": ";".join(
                    [
                        "call:true()",
                        "control:perm(Developer)",
                        "delete:perm(Admin)",
                        "drop:holds()",
                        "edit:perm(Admin)",
                        "examine:perm(Builder)",
                        "get:all()",
                        "puppet:pperm(Developer)",
                        "teleport:true()",
                        "teleport_here:true()",
                        "tell:perm(Admin)",
                        "view:all()",
                    ]
                ),
                "prototype_desc": "Built from Obj",
                "prototype_key": Something,
                "prototype_locks": "spawn:all();edit:all()",
                "prototype_tags": [],
                "tags": [("foo", None, None)],
                "typeclass": "evennia.objects.objects.DefaultObject",
            }

expected_diff_spawned_prototype = {
                "aliases": ["foo"],
                "attrs": [
                    ("desc", "changed desc", None, ""),
                    ("oldtest", "to_keep", None, ""),
                    ("test", "testval", None, ""),
                ],
                "key": "Obj",
                "home": Something,
                "location": Something,
                "locks": ";".join(
                    [
                        "call:true()",
                        "control:perm(Developer)",
                        "delete:perm(Admin)",
                        "drop:holds()",
                        "edit:perm(Admin)",
                        "examine:perm(Builder)",
                        "get:all()",
                        "puppet:pperm(Developer)",
                        "teleport:true()",
                        "teleport_here:true()",
                        "tell:perm(Admin)",
                        "view:all()",
                    ]
                ),
                "prototype_desc": "Built from Obj",
                "prototype_key": Something,
                "prototype_locks": "spawn:all();edit:all()",
                "prototype_tags": [],
                "tags": [("footag", "foocategory", None)],
                "typeclass": "evennia.objects.objects.DefaultObject",
            }

expected_modified_prototype = {
                "attrs": [("oldtest", "to_keep", None, ""), ("fooattr", "fooattrval", None, "")],
                "home": Something,
                "key": "Obj",
                "location": Something,
                "locks": ";".join(
                    [
                        "call:true()",
                        "control:perm(Developer)",
                        "delete:perm(Admin)",
                        "drop:holds()",
                        "edit:perm(Admin)",
                        "examine:perm(Builder)",
                        "get:all()",
                        "puppet:pperm(Developer)",
                        "teleport:true()",
                        "teleport_here:true()",
                        "tell:perm(Admin)",
                        "view:all()",
                    ]
                ),
                "new": "new_val",
                "permissions": ["Builder"],
                "prototype_desc": "New version of prototype",
                "prototype_key": Something,
                "prototype_locks": "spawn:all();edit:all()",
                "prototype_tags": [],
                "test": "testval_changed",
                "typeclass": "evennia.objects.objects.DefaultObject",
            }

expected_prototype_diff = {
                "home": (Something, Something, "KEEP"),
                "prototype_locks": ("spawn:all();edit:all()", "spawn:all();edit:all()", "KEEP"),
                "prototype_key": (Something, Something, "UPDATE"),
                "location": (Something, Something, "KEEP"),
                "locks": (
                    ";".join(
                        [
                            "call:true()",
                            "control:perm(Developer)",
                            "delete:perm(Admin)",
                            "drop:holds()",
                            "edit:perm(Admin)",
                            "examine:perm(Builder)",
                            "get:all()",
                            "puppet:pperm(Developer)",
                            "teleport:true()",
                            "teleport_here:true()",
                            "tell:perm(Admin)",
                            "view:all()",
                        ]
                    ),
                    ";".join(
                        [
                            "call:true()",
                            "control:perm(Developer)",
                            "delete:perm(Admin)",
                            "drop:holds()",
                            "edit:perm(Admin)",
                            "examine:perm(Builder)",
                            "get:all()",
                            "puppet:pperm(Developer)",
                            "teleport:true()",
                            "teleport_here:true()",
                            "tell:perm(Admin)",
                            "view:all()",
                        ]
                    ),
                    "KEEP",
                ),
                "prototype_tags": (None, None, "KEEP"),
                "attrs": {
                    "oldtest": (
                        ("oldtest", "to_keep", None, ""),
                        ("oldtest", "to_keep", None, ""),
                        "KEEP",
                    ),
                    "desc": (("desc", "changed desc", None, ""), None, "KEEP"),
                    "fooattr": (Something, ("fooattr", "fooattrval", None, ""), "ADD"),
                    "test": (
                        ("test", "testval", None, ""),
                        ("test", "testval_changed", None, ""),
                        "UPDATE",
                    ),
                    "new": (Something, ("new", "new_val", None, ""), "ADD"),
                },
                "key": ("Obj", "Obj", "KEEP"),
                "typeclass": (
                    "evennia.objects.objects.DefaultObject",
                    "evennia.objects.objects.DefaultObject",
                    "KEEP",
                ),
                "aliases": {"foo": ("foo", None, "REMOVE")},
                "tags": {"footag": (("footag", "foocategory", None), None, "REMOVE")},
                "prototype_desc": ("Built from Obj", "New version of prototype", "UPDATE"),
                "permissions": {"Builder": (None, "Builder", "ADD")},
            }

expected_flattened_prototype_diff = {
                "aliases": "REMOVE",
                "attrs": "UPDATE",
                "home": "KEEP",
                "key": "KEEP",
                "location": "KEEP",
                "locks": "KEEP",
                "permissions": "UPDATE",
                "prototype_desc": "UPDATE",
                "prototype_key": "UPDATE",
                "prototype_locks": "KEEP",
                "prototype_tags": "KEEP",
                "tags": "REMOVE",
                "typeclass": "KEEP",
            }

expected_prototype_from_updated_object = {
                "aliases": ["foo"],
                "attrs": [
                    ("desc", "changed desc", None, ""),
                    ("fooattr", "fooattrval", None, ""),
                    ("new", "new_val", None, ""),
                    ("oldtest", "to_keep", None, ""),
                    ("test", "testval_changed", None, ""),
                ],
                "home": Something,
                "key": "Obj",
                "location": Something,
                "locks": ";".join(
                    [
                        "call:true()",
                        "control:perm(Developer)",
                        "delete:perm(Admin)",
                        "drop:holds()",
                        "edit:perm(Admin)",
                        "examine:perm(Builder)",
                        "get:all()",
                        "puppet:pperm(Developer)",
                        "teleport:true()",
                        "teleport_here:true()",
                        "tell:perm(Admin)",
                        "view:all()",
                    ]
                ),
                "tags": [("footag", "foocategory", None), (Something, "from_prototype", None)],
                "permissions": ["builder"],
                "prototype_desc": "Built from Obj",
                "prototype_key": Something,
                "prototype_locks": "spawn:all();edit:all()",
                "prototype_tags": [],
                "typeclass": "evennia.objects.objects.DefaultObject",
            }

_PROTPARENTS = {
    "NOBODY": {},
    "GOBLIN": {
        "prototype_key": "GOBLIN",
        "typeclass": "evennia.objects.objects.DefaultObject",
        "key": "goblin grunt",
        "health": lambda: randint(1, 1),
        "resists": ["cold", "poison"],
        "attacks": ["fists"],
        "weaknesses": ["fire", "light"],
    },
    "GOBLIN_WIZARD": {
        "prototype_parent": "GOBLIN",
        "key": "goblin wizard",
        "spells": ["fire ball", "lighting bolt"],
    },
    "GOBLIN_ARCHER": {
        "prototype_parent": "GOBLIN",
        "key": "goblin archer",
        "attacks": ["short bow"],
    },
    "ARCHWIZARD": {"prototype_parent": "GOBLIN", "attacks": ["archwizard staff"]},
    "GOBLIN_ARCHWIZARD": {
        "key": "goblin archwizard",
        "prototype_parent": ("GOBLIN_WIZARD", "ARCHWIZARD"),
    },
    "ISSUE2908": {
        "typeclass": "evennia.objects.objects.DefaultObject",
        "key": "testobject_isse2909",
        "location": "$choice($objlist(",
    },
}
