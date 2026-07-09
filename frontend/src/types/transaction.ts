export interface Transaction {
  id: string;
  asset_symbol: string;
  type: "BUY" | "SELL";
  quantity: number;
  price: number;
  fee: number;
  total_value: number;
  created_at: string;
  note: string;
}