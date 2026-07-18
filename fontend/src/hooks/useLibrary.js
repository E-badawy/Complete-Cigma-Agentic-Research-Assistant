import { useEffect, useState } from "react";
import { getLibraries } from "../services/libraryApi";

export default function useLibrary() {

    const [libraries, setLibraries] = useState([]);

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        loadLibraries();

    }, []);

    async function loadLibraries() {

        try {

            const data = await getLibraries();

            setLibraries(data);

        }

        catch (err) {

            console.error(err);

        }

        finally {

            setLoading(false);

        }

    }

    return {

        libraries,

        loading,

        refreshLibraries: loadLibraries,

    };

}