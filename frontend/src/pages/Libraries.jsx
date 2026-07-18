import { useRef, useState } from "react";
import useLibrary from "../hooks/useLibrary";
import {
    uploadLibrary,
    deleteLibrary,
} from "../services/libraryApi";

function Libraries() {

    const {

        libraries,

        refreshLibraries,

    } = useLibrary();

    const [libraryName, setLibraryName] = useState("");

    const [loading, setLoading] = useState(false);

    const fileInput = useRef(null);

    async function handleUpload() {

        if (!libraryName.trim()) {

            alert("Enter a library name.");

            return;

        }

        if (!fileInput.current.files.length) {

            alert("Select one or more PDF files.");

            return;

        }

        const formData = new FormData();

        formData.append("name", libraryName);

        Array.from(fileInput.current.files).forEach(file => {

            formData.append("files", file);

        });

        try {

            setLoading(true);

            await uploadLibrary(formData);

            alert("Library created successfully.");

            setLibraryName("");

            fileInput.current.value = "";

            refreshLibraries();

        }

        catch (err) {

            console.error(err);

            alert("Upload failed.");

        }

        finally {

            setLoading(false);

        }

    }

    async function handleDelete(name) {

        if (!window.confirm(`Delete ${name}?`)) return;

        try {

            await deleteLibrary(name);

            refreshLibraries();

        }

        catch (err) {

            console.error(err);

            alert("Delete failed.");

        }

    }

    return (

        <div className="space-y-8">

            <div className="bg-white rounded-2xl shadow-lg p-8">

                <h2 className="text-3xl font-bold mb-6">

                    Research Libraries

                </h2>

                <div className="space-y-5">

                    <div>

                        <label className="block font-semibold mb-2">

                            Library Name

                        </label>

                        <input

                            type="text"

                            value={libraryName}

                            onChange={(e)=>setLibraryName(e.target.value)}

                            className="w-full border rounded-xl p-3"

                            placeholder="Example: Tuberculosis"

                        />

                    </div>

                    <div>

                        <label className="block font-semibold mb-2">

                            Upload PDFs

                        </label>

                        <input

                            ref={fileInput}

                            type="file"

                            multiple

                            accept=".pdf"

                            className="w-full"

                        />

                    </div>

                    <button

                        onClick={handleUpload}

                        disabled={loading}

                        className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-xl"

                    >

                        {

                            loading

                            ?

                            "Uploading..."

                            :

                            "Create Library"

                        }

                    </button>

                </div>

            </div>

            <div className="bg-white rounded-2xl shadow-lg p-8">

                <h2 className="text-2xl font-bold mb-6">

                    Existing Libraries

                </h2>

                {

                    libraries.length === 0

                    ?

                    <p>No libraries found.</p>

                    :

                    <div className="grid md:grid-cols-2 gap-6">

                        {

                            libraries.map((library)=>(

                                <div

                                    key={library.library_name}

                                    className="border rounded-xl p-5"

                                >

                                    <h3 className="text-xl font-bold">

                                        {library.library_name}

                                    </h3>

                                    <p className="mt-3">

                                        📄 Documents: {library.documents}

                                    </p>

                                    <p>

                                        🧩 Chunks: {library.chunks}

                                    </p>

                                    <p>

                                        🤖 LLM: {library.llm}

                                    </p>

                                    <p>

                                        🔎 Embeddings:

                                        {" "}

                                        {library.embedding_model}

                                    </p>

                                    <button

                                        onClick={() => handleDelete(library.library_name)}

                                        className="mt-5 bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded-lg"

                                    >

                                        Delete Library

                                    </button>

                                </div>

                            ))

                        }

                    </div>

                }

            </div>

        </div>

    );

}

export default Libraries;