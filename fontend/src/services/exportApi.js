import jsPDF from "jspdf";
import { saveAs } from "file-saver";
import { Document, Packer, Paragraph } from "docx";

export function copyReport(text) {
    navigator.clipboard.writeText(text);
}

export function downloadMarkdown(text) {
    const blob = new Blob([text], {
        type: "text/markdown;charset=utf-8"
    });

    saveAs(blob, "research-report.md");
}

export async function downloadWord(text) {

    const doc = new Document({

        sections: [
            {
                children: [
                    new Paragraph(text)
                ]
            }
        ]

    });

    const blob = await Packer.toBlob(doc);

    saveAs(blob, "research-report.docx");

}

export function downloadPDF(text) {

    const pdf = new jsPDF();

    pdf.setFontSize(12);

    pdf.text(text, 10, 10, {
        maxWidth: 180
    });

    pdf.save("research-report.pdf");

}