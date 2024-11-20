from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 36)
        self.cell(0, 10, "CS50 Shirtificate", align="C", ln=True)
        self.ln(25)


def create_shirtificate(name):
    pdf = PDF()
    pdf.add_page()
    pdf.image("shirtificate.png", x=10, w=190)
    pdf.set_font("Arial", "B", 40)
    pdf.set_text_color(255, 255, 255)
    name_width = pdf.get_string_width(name)
    pdf.set_xy((pdf.w - name_width) / 2, 100)
    pdf.cell(name_width, 10, name)
    pdf.output("shirtificate.pdf")


def main():
    name = input("Enter your name: ")
    create_shirtificate(f"{name} took CS50")


if __name__ == "__main__":
    main()
