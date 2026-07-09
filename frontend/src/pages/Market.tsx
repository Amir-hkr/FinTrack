import { useQuery } from "@tanstack/react-query";

import { getMarketPrice } from "../api/market";

import Card from "../components/common/Card";


const coins = [
  "BTC",
  "ETH",
  "SOL",
  "ADA",
];


function Market() {

  return (
    <>
      <h1 className="text-3xl font-bold mb-6">
        Market Prices
      </h1>


      <div className="grid grid-cols-1 md:grid-cols-2 gap-5">

        {coins.map((coin) => (
          <MarketCard
            key={coin}
            symbol={coin}
          />
        ))}

      </div>
    </>
  );
}


function MarketCard({
  symbol,
}: {
  symbol: string;
}) {

  const {
    data,
    isLoading,
  } = useQuery({
    queryKey: ["market", symbol],
    queryFn: () => getMarketPrice(symbol),
    
  });


  if (isLoading) {
    return (
      <Card>
        Loading {symbol}...
      </Card>
    );
  }


  return (
    <Card>
      <div className="flex justify-between items-center">

        <h2 className="text-xl font-bold">
          {symbol}
        </h2>

        <span className="text-green-600 font-semibold">
          LIVE
        </span>

      </div>


      <p className="text-3xl font-bold mt-4">
        ${data.price.toLocaleString()}
      </p>


      <p className="text-gray-500 mt-2">
        USD Price
      </p>

    </Card>
  );
}


export default Market;