import { useState } from "react";

import {
  useQuery,
  useMutation,
  useQueryClient,
} from "@tanstack/react-query";

import {
  getTransactions,
  createTransaction,
  deleteTransaction,
} from "../api/transactions";

import { getAssets } from "../api/assets";

import Card from "../components/common/Card";
import Button from "../components/common/Button";

import type { Asset } from "../types/asset";
import type { Transaction } from "../types/transaction";


function Transactions() {

  const queryClient = useQueryClient();


  const [showForm, setShowForm] =
    useState(false);


  const [search, setSearch] =
    useState("");


  const [filterType, setFilterType] =
    useState<"ALL" | "BUY" | "SELL">(
      "ALL"
    );


  const [asset, setAsset] =
    useState("");


  const [type, setType] =
    useState<"BUY" | "SELL">(
      "BUY"
    );


  const [quantity, setQuantity] =
    useState<number | "">("");


  const [price, setPrice] =
    useState<number | "">("");


  const [fee, setFee] =
    useState<number | "">("");


  const [note, setNote] =
    useState("");



  const {
    data: transactions = [],
    isLoading,
  } = useQuery({
    queryKey: ["transactions"],
    queryFn: getTransactions,
  });



  const {
    data: assets = [],
  } = useQuery({
    queryKey: ["assets"],
    queryFn: getAssets,
  });



  const createMutation =
    useMutation({

      mutationFn:
        createTransaction,


      onSuccess: () => {

        queryClient.invalidateQueries({
          queryKey: [
            "transactions",
          ],
        });


        queryClient.invalidateQueries({
          queryKey: [
            "portfolio",
          ],
        });


        queryClient.invalidateQueries({
          queryKey: [
            "analytics-summary",
          ],
        });


        setShowForm(false);
        setAsset("");
        setType("BUY");
        setQuantity("");
        setPrice("");
        setFee("");
        setNote("");

      },

    });



  const deleteMutation =
    useMutation({

      mutationFn:
        deleteTransaction,


      onSuccess: () => {

        queryClient.invalidateQueries({
          queryKey: [
            "transactions",
          ],
        });


        queryClient.invalidateQueries({
          queryKey: [
            "portfolio",
          ],
        });


        queryClient.invalidateQueries({
          queryKey: [
            "analytics-summary",
          ],
        });

      },

    });



  const filteredTransactions =
    transactions
      .filter(
        (t: Transaction) => {

          const matchSearch =
            t.asset_symbol
              .toLowerCase()
              .includes(
                search.toLowerCase()
              );


          const matchType =
            filterType === "ALL"
              ? true
              : t.type === filterType;


          return (
            matchSearch &&
            matchType
          );

        }
      )
      .sort(
        (
          a: Transaction,
          b: Transaction
        ) =>
          new Date(
            b.created_at
          ).getTime()
          -
          new Date(
            a.created_at
          ).getTime()
      );



  const handleSave = () => {

    if (!asset) {
      alert(
        "Please select an asset."
      );
      return;
    }


    if (
      quantity === "" ||
      price === "" ||
      quantity <= 0 ||
      price <= 0
    ) {

      alert(
        "Quantity and Price must be greater than zero."
      );

      return;
    }


    createMutation.mutate({

      asset_symbol:
        asset,

      type,

      quantity,

      price,

      fee:
        fee === ""
          ? 0
          : fee,

      note,

    });

  };

  if (isLoading) {
    return (
      <h2>
        Loading...
      </h2>
    );
  }


  return (
    <>
      <div className="flex justify-between items-center mb-6">

        <h1 className="text-3xl font-bold">
          Transactions
        </h1>


        <Button
          onClick={() =>
            setShowForm(!showForm)
          }
        >
          + New Transaction
        </Button>

      </div>



      {showForm && (

        <Card>

          <div className="grid md:grid-cols-2 gap-4">


            <select
              className="border rounded-lg p-2"
              value={asset}
              onChange={(e) =>
                setAsset(
                  e.target.value
                )
              }
            >

              <option value="">
                Select Asset
              </option>


              {assets.map(
                (a: Asset) => (

                  <option
                    key={a.id}
                    value={a.symbol}
                  >
                    {a.name} ({a.symbol})
                  </option>

                )
              )}

            </select>



            <select
              className="border rounded-lg p-2"
              value={type}
              onChange={(e) =>
                setType(
                  e.target.value as
                    | "BUY"
                    | "SELL"
                )
              }
            >

              <option value="BUY">
                BUY
              </option>


              <option value="SELL">
                SELL
              </option>


            </select>



            <input
              type="number"
              className="border rounded-lg p-2"
              placeholder="Amount (Quantity)"
              value={quantity}
              onChange={(e) =>
                setQuantity(
                  e.target.value === ""
                    ? ""
                    : Number(
                        e.target.value
                      )
                )
              }
            />



            <input
              type="number"
              className="border rounded-lg p-2"
              placeholder="Price per unit ($)"
              value={price}
              onChange={(e) =>
                setPrice(
                  e.target.value === ""
                    ? ""
                    : Number(
                        e.target.value
                      )
                )
              }
            />



            <input
              type="number"
              className="border rounded-lg p-2"
              placeholder="Transaction Fee ($)"
              value={fee}
              onChange={(e) =>
                setFee(
                  e.target.value === ""
                    ? ""
                    : Number(
                        e.target.value
                      )
                )
              }
            />



            <input
              className="border rounded-lg p-2"
              placeholder="Note"
              value={note}
              onChange={(e) =>
                setNote(
                  e.target.value
                )
              }
            />


          </div>



          <div className="mt-5">

            <Button
              disabled={
                createMutation.isPending
              }
              onClick={handleSave}
            >

              {
                createMutation.isPending
                  ? "Saving..."
                  : "Save Transaction"
              }

            </Button>

          </div>


        </Card>

      )}




      <div className="flex gap-4 mb-4">


        <input
          className="
            border
            p-2
            rounded-lg
            flex-1
          "
          placeholder="Search transaction..."
          value={search}
          onChange={(e) =>
            setSearch(
              e.target.value
            )
          }
        />



        <select
          className="
            border
            p-2
            rounded-lg
          "
          value={filterType}
          onChange={(e) =>
            setFilterType(
              e.target.value as
                | "ALL"
                | "BUY"
                | "SELL"
            )
          }
        >

          <option value="ALL">
            All
          </option>


          <option value="BUY">
            BUY
          </option>


          <option value="SELL">
            SELL
          </option>


        </select>


      </div>

      <Card>

        <table className="w-full text-center">


          <thead>

            <tr className="border-b">

              <th className="py-3">
                Asset
              </th>


              <th>
                Type
              </th>


              <th>
                Qty
              </th>


              <th>
                Price
              </th>


              <th>
                Total
              </th>


              <th>
                Date
              </th>


              <th>
                Action
              </th>


            </tr>

          </thead>



          <tbody>


            {filteredTransactions.length === 0 ? (

              <tr>

                <td
                  colSpan={7}
                  className="
                    text-center
                    py-5
                    text-gray-500
                  "
                >
                  No transactions found
                </td>

              </tr>


            ) : (


              filteredTransactions.map(
                (t: Transaction) => (

                  <tr
                    key={t.id}
                    className="
                      border-b
                      hover:bg-gray-50
                    "
                  >


                    <td className="py-3 font-semibold">
                      {t.asset_symbol}
                    </td>



                    <td>

                      <span
                        className={`
                          px-3
                          py-1
                          rounded-full
                          text-white
                          text-sm
                          font-semibold
                          ${
                            t.type === "BUY"
                              ? "bg-green-500"
                              : "bg-red-500"
                          }
                        `}
                      >

                        {t.type}

                      </span>

                    </td>



                    <td>
                      {t.quantity}
                    </td>



                    <td>

                      {new Intl.NumberFormat(
                        "en-US",
                        {
                          style:
                            "currency",
                          currency:
                            "USD",
                        }
                      ).format(
                        t.price
                      )}

                    </td>



                    <td className="font-semibold">

                      {new Intl.NumberFormat(
                        "en-US",
                        {
                          style:
                            "currency",
                          currency:
                            "USD",
                        }
                      ).format(
                        t.total_value
                      )}

                    </td>



                    <td>

                      {new Date(
                        t.created_at
                      ).toLocaleDateString(
                        "en-US"
                      )}

                    </td>



                    <td>

                      <button
                        disabled={
                          deleteMutation.isPending
                        }
                        onClick={() => {

                          const confirmDelete =
                            window.confirm(
                              "Delete this transaction?"
                            );


                          if (confirmDelete) {

                            deleteMutation.mutate(
                              t.id
                            );

                          }

                        }}
                        className="
                          bg-red-500
                          hover:bg-red-600
                          disabled:opacity-50
                          text-white
                          px-3
                          py-1
                          rounded-lg
                          transition
                        "
                      >

                        {
                          deleteMutation.isPending
                            ? "Deleting..."
                            : "Delete"
                        }

                      </button>


                    </td>


                  </tr>

                )

              )


            )}


          </tbody>


        </table>


      </Card>


    </>
  );
}


export default Transactions;