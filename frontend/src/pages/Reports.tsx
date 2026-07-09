import { useQuery } from "@tanstack/react-query";

import { getPortfolio } from "../api/portfolio";

import Card from "../components/common/Card";
import Button from "../components/common/Button";

import {
  exportCSV,
  exportExcel,
  exportPDF,
} from "../utils/report";

function Reports() {
  const { data = [], isLoading, isError } = useQuery({
    queryKey: ["portfolio"],
    queryFn: getPortfolio,
  });

  if (isLoading) {
    return <h2>Loading...</h2>;
  }

  if (isError) {
    return <h2>Error loading reports.</h2>;
  }

  return (
    <>
      <h1 className="text-3xl font-bold mb-6">
        Reports
      </h1>

      <div className="flex gap-4 mb-6">
        <Button onClick={() => exportCSV(data)}>
          Export CSV
        </Button>

        <Button onClick={() => exportExcel(data)}>
          Export Excel
        </Button>

        <Button onClick={() => exportPDF(data)}>
          Export PDF
        </Button>
      </div>

      <Card>
        <table className="w-full">
          <thead>
            <tr className="border-b">
              <th className="py-3">Asset</th>
              <th>Quantity</th>
              <th>Current Price</th>
              <th>Current Value</th>
              <th>Profit / Loss</th>
            </tr>
          </thead>

          <tbody>
            {data.map((item: any) => (
              <tr
                key={item.asset_symbol}
                className="border-b text-center"
              >
                <td>{item.asset_symbol}</td>

                <td>{item.quantity}</td>

                <td>
                  ${item.current_price.toLocaleString()}
                </td>

                <td>
                  ${item.current_value.toLocaleString()}
                </td>

                <td
                  className={
                    item.profit_loss >= 0
                      ? "text-green-600 font-bold"
                      : "text-red-600 font-bold"
                  }
                >
                  ${item.profit_loss.toFixed(2)}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Card>
    </>
  );
}

export default Reports;