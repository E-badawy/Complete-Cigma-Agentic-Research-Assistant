function Settings() {

    return (

        <div className="space-y-8">

            <div className="bg-white rounded-2xl shadow-lg p-8">

                <h2 className="text-3xl font-bold mb-8">

                    Settings

                </h2>

                <div className="space-y-6">

                    <div>

                        <label className="font-semibold block mb-2">

                            Large Language Model

                        </label>

                        <input

                            value="llama-3.3-70b-versatile"

                            disabled

                            className="w-full border rounded-xl p-3 bg-gray-100"

                        />

                    </div>

                    <div>

                        <label className="font-semibold block mb-2">

                            Embedding Model

                        </label>

                        <input

                            value="BAAI/bge-small-en-v1.5"

                            disabled

                            className="w-full border rounded-xl p-3 bg-gray-100"

                        />

                    </div>

                    <div>

                        <label className="font-semibold block mb-2">

                            Retrieval Engine

                        </label>

                        <input

                            value="FAISS + Semantic Reranking"

                            disabled

                            className="w-full border rounded-xl p-3 bg-gray-100"

                        />

                    </div>

                    <div>

                        <label className="font-semibold block mb-2">

                            Scientific Search

                        </label>

                        <input

                            value="CrossRef"

                            disabled

                            className="w-full border rounded-xl p-3 bg-gray-100"

                        />

                    </div>

                </div>

            </div>

        </div>

    );

}

export default Settings;