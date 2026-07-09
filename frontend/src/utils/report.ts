import { saveAs } from "file-saver";
import * as XLSX from "xlsx";
import jsPDF from "jspdf";
import autoTable from "jspdf-autotable";

export function exportCSV(data: any[]) {
  const worksheet = XLSX.utils.json_to_sheet(data);
  const csv = XLSX.utils.sheet_to_csv(worksheet);

  const blob = new Blob([csv], {
    type: "text/csv;charset=utf-8;",
  });

  saveAs(blob, "portfolio-report.csv");
}

export function exportExcel(data: any[]) {
  const worksheet = XLSX.utils.json_to_sheet(data);

  const workbook = XLSX.utils.book_new();

  XLSX.utils.book_append_sheet(
    workbook,
    worksheet,
    "Portfolio"
  );

  XLSX.writeFile(workbook, "portfolio-report.xlsx");
}

export function exportPDF(data: any[]) {
  const doc = new jsPDF();

  doc.setFontSize(18);
  doc.text("Portfolio Report", 14, 20);

  autoTable(doc, {
    head: [[
      "Asset",
      "Quantity",
      "Current Price",
      "Current Value",
      "Profit/Loss",
    ]],

    body: data.map((item) => [
      item.asset_symbol,
      item.quantity,
      item.current_price,
      item.current_value,
      item.profit_loss,
    ]),
  });

  doc.save("portfolio-report.pdf");
}