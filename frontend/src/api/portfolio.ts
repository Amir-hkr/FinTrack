import axios from "./axios";

export const getPortfolio = async () => {
  const response = await axios.get("/portfolio");

  return response.data.data;
};