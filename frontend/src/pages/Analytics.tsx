import { useQuery } from "@tanstack/react-query";

import { getPortfolio } from "../api/portfolio";

import ProfitChart from "../components/charts/ProfitChart";
import AllocationChart from "../components/charts/AllocationChart";

function Analytics() {
  const { data = [], isLoading, isError } = useQuery({
    queryKey: ["portfolio"],
    queryFn: getPortfolio,
  });

  if (isLoading) {
    return <h2>Loading...</h2>;
  }

  if (isError) {
    return <h2>Error loading analytics.</h2>;
  }

  return (
    <>
      <h1 className="text-3xl font-bold mb-6">
        Analytics
      </h1>

      <div className="grid grid-cols-1 xl:grid-cols-2 gap-6">
        <ProfitChart data={data} />
        <AllocationChart data={data} />
      </div>
    </>
  );
}

export default Analytics;