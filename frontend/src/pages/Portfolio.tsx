import { useQuery } from "@tanstack/react-query";

import { getPortfolio } from "../api/portfolio";

import Card from "../components/common/Card";

type PortfolioItem = {
  asset_symbol: string;
  quantity: number;
  total_invested: number;
  average_buy_price: number;
  current_price: number;
  current_value: number;
  profit_loss: number;
  profit_percentage: number;
};

function Portfolio() {
  const {
    data = [],
    isLoading,
    isError,
  } = useQuery<PortfolioItem[]>({
    queryKey: ["portfolio"],
    queryFn: getPortfolio,
  });

  if (isLoading) return <h2>Loading...</h2>;

  if (isError) return <h2>Error loading portfolio.</h2>;

  const money = (value: number) =>
    new Intl.NumberFormat("en-US", {
      style: "currency",
      currency: "USD",
    }).format(value);

  return (
    <>
      <h1 className="text-3xl font-bold mb-6">
        Portfolio
      </h1>

      <Card>
        <table className="w-full">
          <thead>
            <tr className="border-b">
              <th className="py-3 text-left">
                Asset
              </th>
              <th>Quantity</th>
              <th>Average Buy</th>
              <th>Current Price</th>
              <th>Value</th>
              <th>Profit/Loss</th>
              <th>Profit %</th>
            </tr>
          </thead>

          <tbody>
            {data.map((item) => (
              <tr
                key={item.asset_symbol}
                className="border-b hover:bg-gray-50 text-center"
              >
                <td className="py-3 font-bold text-left">
                  {item.asset_symbol}
                </td>

                <td>
                  {item.quantity}
                </td>

                <td>
                  {money(item.average_buy_price)}
                </td>

                <td>
                  {money(item.current_price)}
                </td>

                <td className="font-semibold">
                  {money(item.current_value)}
                </td>

                <td
                  className={
                    item.profit_loss >= 0
                      ? "text-green-600 font-semibold"
                      : "text-red-600 font-semibold"
                  }
                >
                  {money(item.profit_loss)}
                </td>

                <td
                  className={
                    item.profit_percentage >= 0
                      ? "text-green-600 font-semibold"
                      : "text-red-600 font-semibold"
                  }
                >
                  {item.profit_percentage.toFixed(2)}%
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Card>
    </>
  );
}

export default Portfolio;