import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from "recharts";

type Props = {
  data: {
    asset_symbol: string;
    profit_loss: number;
  }[];
};

function ProfitChart({ data }: Props) {
  return (
    <div className="bg-white rounded-xl shadow p-5 mt-6">
      <h2 className="text-xl font-bold mb-4">
        Profit / Loss by Asset
      </h2>

      <ResponsiveContainer width="100%" height={350}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="asset_symbol" />

          <YAxis />

          <Tooltip />

          <Bar
            dataKey="profit_loss"
            fill="#2563eb"
            radius={[6, 6, 0, 0]}
          />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default ProfitChart;