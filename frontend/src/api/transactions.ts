import api from "./axios";

export const getTransactions = async () => {
  const response = await api.get("/transactions");
  return response.data.data;
};

export const createTransaction = async (data: {
  asset_symbol: string;
  type: "BUY" | "SELL";
  quantity: number;
  price: number;
  fee: number;
  note: string;
}) => {
  const response = await api.post(
    "/transactions",
    data
  );

  return response.data.data;
};

export const deleteTransaction = async (
  id: string
) => {
  const response = await api.delete(
    `/transactions/${id}`
  );

  return response.data.data;
};