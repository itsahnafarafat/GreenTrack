"use client";

import { useEffect, useState } from "react";
import api from "@/lib/axios";

interface EmissionFactor {
  id: number;
  category: string;
  activity: string;
  unit: string;
  factor: number;
}

export default function Dashboard() {
  const [factors, setFactors] = useState<EmissionFactor[]>([]);

  useEffect(() => {
    async function fetchFactors() {
      try {
        const res = await api.get("/emissionfactors/");
        setFactors(res.data);
      } catch (error) {
        console.error("Failed to fetch emission factors:", error);
      }
    }

    fetchFactors();
  }, []);

  return (
    <main className="p-6 bg-white text-gray-900">
      <h1 className="text-3xl font-bold mb-4">📊 Emission Factors</h1>
      <ul className="space-y-2">
        {factors.map((factor) => (
          <li key={factor.id} className="border p-4 rounded shadow">
            <p>
              <strong>{factor.category}:</strong> {factor.activity}
            </p>
            <p>
              Emits <strong>{factor.factor}</strong> kg CO₂ per{" "}
              {factor.unit}
            </p>
          </li>
        ))}
      </ul>
    </main>
  );
}
