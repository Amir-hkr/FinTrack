import axios from "./axios";

export const getMarketPrice = async (symbol: string) => {
  const response = await axios.get(`/market/${symbol}`);
  return response.data;
};