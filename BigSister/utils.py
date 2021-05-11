import re

from BigSister import comunas_chile


def get_comuna_name(identifier: str) -> str:
    return comunas_chile[identifier]


def get_comuna_identifier(comuna_name: str) -> str:
    for identifier, name in comunas_chile.items():
        if name == comuna_name:
            return identifier


def get_padron_csv_name(identifier: str, information: list[str, str, str]) -> str:
    return f"{identifier}__{information[0]}__{information[1]}_p{information[3]}.csv"


def get_padron_csv_information(padron_csv_name: str) -> tuple[str, list[str, str, str]]:
    match = re.match(
        r"A([0.9]+)__([0.9]+)__([0.9]+)_p([0.9]+)\.csv", padron_csv_name)
    groups = match.groups()
    return "A" + groups[0], groups[1::]
