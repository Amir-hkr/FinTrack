import { useQuery } from "@tanstack/react-query";

import { getAnalyticsSummary } from "../api/analytics";
import { getPortfolio } from "../api/portfolio";

import StatCard from "../components/StatCard";
import PortfolioChart from "../components/charts/PortfolioChart";

import type { PortfolioItem } from "../types/portfolio";

function Dashboard() {
  const {
    data: analytics,
    isLoading: analyticsLoading,
    isError: analyticsError,
  } = useQuery({
    queryKey: ["analytics-summary"],
    queryFn: getAnalyticsSummary,
  });

  const {
    data: portfolio = [],
    isLoading: portfolioLoading,
    isError: portfolioError,
  } = useQuery({
    queryKey: ["portfolio"],
    queryFn: getPortfolio,
  });

  if (analyticsLoading || portfolioLoading) {
    return <h2>Loading...</h2>;
  }

  if (analyticsError || portfolioError) {
    return <h2>Error loading dashboard.</h2>;
  }

  return (
    <>
      <h1 className="text-3xl font-bold mb-6">
        Dashboard
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-5 mb-8">
        <StatCard
          title="Total Invested"
          value={`$${analytics.total_invested.toFixed(2)}`}
        />

        <StatCard
          title="Current Value"
          value={`$${analytics.current_value.toFixed(2)}`}
        />

        <StatCard
          title="Profit / Loss"
          value={`$${analytics.total_profit_loss.toFixed(2)}`}
        />

        <StatCard
          title="Profit %"
          value={`${analytics.profit_percentage.toFixed(2)}%`}
        />
      </div>

      <PortfolioChart
        data={portfolio.map((asset: PortfolioItem) => ({
          name: asset.asset_symbol,
          value: asset.current_value,
        }))}
      />
    </>
  );
}

export default Dashboard;