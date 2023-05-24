import click
import pandas
from pathlib import Path


@click.command()
@click.argument(
    "amber_frcmod_path",
    type=click.Path(),
)
def main(amber_frcmod_path):
    ion_nb_params = list()

    nonbonded = False

    with open(Path(amber_frcmod_path), "r") as amber_frcmod_file:
        for line in amber_frcmod_file:
            if line == "\n":
                nonbonded = False

            if nonbonded:
                fields = line.split()

                ion_nb_params.append(
                    {
                        "element": fields[0],
                        "rmin_half (Angstrom)": float(fields[1]),
                        "epsilon (kcal/mol)": float(fields[2]),
                    }
                )

            if line.startswith("NONBON"):
                nonbonded = True

    output_path = Path(
        "openforcefields", "data", f"{Path(amber_frcmod_path).suffix[1:]}.csv"
    )
    pandas.DataFrame(ion_nb_params).set_index("element").to_csv(output_path)


if __name__ == "__main__":
    main()
