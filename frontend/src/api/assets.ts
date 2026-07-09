import api from "./axios";

export const getAssets = async () => {
  const response = await api.get("/assets");
  return response.data.data;
};

export const createAsset = async (data: {
  name: string;
  symbol: string;
  category: string;
}) => {
  const response = await api.post("/assets", data);
  return response.data.data;
};

export const deleteAsset = async (id: string) => {
  const response = await api.delete(`/assets/${id}`);
  return response.data.data;
};