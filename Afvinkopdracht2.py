from flask import Flask, render_template, request
from translate import translate

dna_converter = Flask(__name__)


# URL
@dna_converter.route('/', methods=["POST", "GET"])
def converter():
    dna = request.args.get("dna", "")
    protein = translate(dna)
    return render_template("converter.html", dna=dna, protein=protein)


def main():
    dna_converter.run()


main()
