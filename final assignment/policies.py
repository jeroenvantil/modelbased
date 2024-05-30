policies = [
    Policy(
        "Policy 1 - 2dm per dike",
        **dict(
            get_do_nothing_dict(),
            **{f"A.{i}_DikeIncrease 0": 2 for i in range(1,6)}
        )
    ),
    Policy(
        "Policy 2 - 4dm per dike",
        **dict(
            get_do_nothing_dict(),
            **{f"A.{i}_DikeIncrease 0": 4 for i in range(1,6)}
        )
    ),
    Policy(
        "Policy 3 - 6 dm per dike",
        **dict(
            get_do_nothing_dict(),
            **{f"A.{i}_DikeIncrease 0": 6 for i in range(1,6)}
        )
    ),
    Policy(
        "Policy 4 - 8 dm per dike",
        **dict(
            get_do_nothing_dict(),
            **{f"A.{i}_DikeIncrease 0": 8 for i in range(1,6)}
        )
    )
    Policy(
        "Policy 5 - 10 dm per dike",
        **dict(
            get_do_nothing_dict(),
            **{f"A.{i}_DikeIncrease 0": 10 for i in range(1, 6)}
        )
    )
]