export interface PortfolioItem {
  asset_symbol: string;
  quantity: number;
  total_invested: number;
  average_buy_price: number;
  current_price: number;
  current_value: number;
  profit_loss: number;
  profit_percentage: number;
}