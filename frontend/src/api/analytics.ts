import axios from "./axios";

export const getAnalyticsSummary = async () => {
  const response = await axios.get("/analytics/summary");

  return response.data.data;
};