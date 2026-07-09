import { useState } from "react";
import {
  useQuery,
  useMutation,
  useQueryClient,
} from "@tanstack/react-query";

import {
  getAssets,
  createAsset,
  deleteAsset,
} from "../api/assets";

import Card from "../components/common/Card";
import Badge from "../components/common/Badge";
import Button from "../components/common/Button";

import type { Asset } from "../types/asset";

function Assets() {
  const queryClient = useQueryClient();

  const [name, setName] = useState("");
  const [symbol, setSymbol] = useState("");
  const [category, setCategory] = useState("");
  const [search, setSearch] = useState("");

  const [showForm, setShowForm] =
    useState(false);

  const {
    data: assets = [],
    isLoading,
    isError,
  } = useQuery({
    queryKey: ["assets"],
    queryFn: getAssets,
  });


  const createMutation = useMutation({
    mutationFn: createAsset,

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["assets"],
      });

      setName("");
      setSymbol("");
      setCategory("");
      setShowForm(false);
    },
  });


  const deleteMutation = useMutation({
    mutationFn: deleteAsset,

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["assets"],
      });
    },
  });


  const filteredAssets = assets.filter(
    (asset: Asset) =>
      asset.name
        .toLowerCase()
        .includes(
          search.toLowerCase()
        ) ||
      asset.symbol
        .toLowerCase()
        .includes(
          search.toLowerCase()
        ) ||
      asset.category
        .toLowerCase()
        .includes(
          search.toLowerCase()
        )
  );


  if (isLoading) {
    return <h2>Loading...</h2>;
  }


  if (isError) {
    return (
      <h2>
        Error loading assets.
      </h2>
    );
  }


  return (
    <>
      <div className="flex justify-between items-center mb-6">

        <h1 className="text-3xl font-bold">
          Assets
        </h1>


        <Button
          onClick={() =>
            setShowForm(!showForm)
          }
        >
          + Add Asset
        </Button>

      </div>


      {showForm && (
        <Card>

          <div className="grid grid-cols-3 gap-4 mb-4">

            <input
              className="border p-2 rounded"
              placeholder="Name"
              value={name}
              onChange={(e) =>
                setName(e.target.value)
              }
            />


            <input
              className="border p-2 rounded"
              placeholder="Symbol"
              value={symbol}
              onChange={(e) =>
                setSymbol(e.target.value)
              }
            />


            <input
              className="border p-2 rounded"
              placeholder="Category"
              value={category}
              onChange={(e) =>
                setCategory(e.target.value)
              }
            />

          </div>


          <Button
            onClick={() =>
              createMutation.mutate({
                name,
                symbol,
                category,
              })
            }
          >
            {
              createMutation.isPending
                ? "Saving..."
                : "Save Asset"
            }
          </Button>


        </Card>
      )}


      <input
        className="
          border
          p-2
          rounded-lg
          mb-4
          w-full
        "
        placeholder="Search asset..."
        value={search}
        onChange={(e) =>
          setSearch(e.target.value)
        }
      />


      <Card>

        <table className="w-full">

          <thead>

            <tr className="border-b">

              <th className="text-left py-3">
                Symbol
              </th>

              <th className="text-left py-3">
                Name
              </th>

              <th className="text-left py-3">
                Category
              </th>

              <th className="text-center py-3">
                Action
              </th>

            </tr>

          </thead>


          <tbody>

            {filteredAssets.length === 0 ? (

              <tr>

                <td
                  colSpan={4}
                  className="text-center py-5 text-gray-500"
                >
                  No assets found
                </td>

              </tr>

            ) : (

              filteredAssets.map(
                (asset: Asset) => (

                  <tr
                    key={asset.id}
                    className="
                      border-b
                      hover:bg-gray-50
                    "
                  >

                    <td className="py-3 font-semibold">
                      {asset.symbol}
                    </td>


                    <td>
                      {asset.name}
                    </td>


                    <td>
                      <Badge
                        text={asset.category}
                      />
                    </td>


                    <td className="text-center">

                      <button
                        disabled={
                          deleteMutation.isPending
                        }
                        onClick={() => {

                          if (
                            window.confirm(
                              `Delete ${asset.symbol}?`
                            )
                          ) {

                            deleteMutation.mutate(
                              asset.id
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
                          rounded
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

export default Assets;