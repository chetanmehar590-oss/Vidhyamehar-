import React, { useState } from 'react';
import { Button } from '../components/ui/button';
import { Input } from '../components/ui/input';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../components/ui/select';
import { Checkbox } from '../components/ui/checkbox';
import { toast } from '../hooks/use-toast';
import { Dices, Coins, TrendingDown, Settings2, Check } from 'lucide-react';
import axios from 'axios';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

const TableBooking = () => {
  const [amount, setAmount] = useState('');
  const [type, setType] = useState('Full');
  const [gamePlus, setGamePlus] = useState('');
  const [username, setUsername] = useState('');
  const [options, setOptions] = useState({
    freshId: false,
    codeAapDoge: false,
    noIPhone: false,
    noKingPass: false,
    autoLoss: false
  });
  const [balance] = useState(28.00);
  const [lastTable] = useState({
    amount: 600,
    type: 'Full',
    gamePlus: 0,
    options: 'None'
  });
  const [loading, setLoading] = useState(false);

  const amountOptions = [1000, 2000, 3000, 5000, 7000, 8000, 10000];
  const gamePlusOptions = ['100+', '200+', '500+', '1000+'];

  const handleOptionChange = (optionKey) => {
    setOptions(prev => ({
      ...prev,
      [optionKey]: !prev[optionKey]
    }));
  };

  const handleSubmit = async () => {
    if (!amount) {
      toast({
        title: 'Error',
        description: 'Please enter amount',
        variant: 'destructive'
      });
      return;
    }

    setLoading(true);
    try {
      const response = await axios.post(`${API}/send-table`, {
        username: username || 'User',
        amount,
        type,
        gamePlus: gamePlus || '0',
        options
      });

      if (response.data.success) {
        toast({
          title: 'Success',
          description: 'Table request sent to group!'
        });
        // Reset form
        setAmount('');
        setGamePlus('');
        setUsername('');
        setOptions({
          freshId: false,
          codeAapDoge: false,
          noIPhone: false,
          noKingPass: false,
          autoLoss: false
        });
      }
    } catch (error) {
      toast({
        title: 'Error',
        description: error.response?.data?.detail || 'Failed to send table request',
        variant: 'destructive'
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      {/* Header */}
      <div className="bg-white border-b shadow-sm">
        <div className="max-w-4xl mx-auto px-4 py-4 flex items-center gap-3">
          <div className="w-12 h-12 bg-gradient-to-br from-green-600 to-green-800 rounded-full flex items-center justify-center">
            <Dices className="w-6 h-6 text-white" />
          </div>
          <h1 className="text-2xl font-bold tracking-wide">DEEP NIGHT LUDO CLUB</h1>
        </div>
      </div>

      <div className="max-w-4xl mx-auto px-4 py-6">
        {/* Balance Section */}
        <div className="bg-white rounded-lg shadow-md p-4 mb-6 flex justify-between items-center">
          <h2 className="text-xl font-bold">Table Details</h2>
          <div className="flex items-center gap-2">
            <div className="w-6 h-6 bg-green-500 rounded flex items-center justify-center text-white text-xs font-bold">₹</div>
            <span className="text-xl font-bold">Balance: ₹{balance.toFixed(2)}</span>
          </div>
        </div>

        {/* Last Table Request */}
        <div className="bg-white rounded-2xl shadow-md p-6 mb-6 border-2 border-gray-200">
          <div className="flex items-start gap-3 mb-4">
            <div className="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center">
              <span className="text-blue-600 font-bold">1</span>
            </div>
            <div className="flex-1">
              <h3 className="text-xl font-bold mb-2">Last Table Request</h3>
              <div className="flex items-center gap-4 text-lg mb-3">
                <span className="flex items-center gap-2">
                  <Coins className="w-5 h-5 text-yellow-600" />
                  <span className="font-bold">₹{lastTable.amount}.00</span>
                </span>
                <span className="flex items-center gap-2">
                  <Dices className="w-5 h-5 text-green-600" />
                  <span className="font-bold">{lastTable.type}</span>
                </span>
                <span className="flex items-center gap-2">
                  <TrendingDown className="w-5 h-5 text-red-600" />
                  <span className="font-bold">{lastTable.gamePlus}</span>
                </span>
              </div>
              <div className="flex items-center gap-2 text-base">
                <Settings2 className="w-4 h-4 text-blue-600" />
                <span className="font-semibold">Options: {lastTable.options}</span>
              </div>
            </div>
          </div>

          <div className="flex gap-3">
            <Button variant="outline" className="flex-1 h-12 text-base font-semibold rounded-full">
              <span className="text-xl mr-2">🔄</span>
              Copy Table
            </Button>
            <Button variant="outline" className="flex-1 h-12 text-base font-semibold rounded-full">
              <span className="text-xl mr-2">✏️</span>
              Edit Table
            </Button>
          </div>
        </div>

        {/* Username Input */}
        <div className="bg-white rounded-lg shadow-md p-6 mb-6">
          <label className="flex items-center gap-2 text-lg font-bold mb-3">
            <span className="text-xl">👤</span>
            Your Name
          </label>
          <Input
            type="text"
            placeholder="Enter your name"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="h-14 text-lg"
          />
        </div>

        {/* Amount Section */}
        <div className="bg-white rounded-lg shadow-md p-6 mb-6">
          <label className="flex items-center gap-2 text-lg font-bold mb-3">
            <Coins className="w-6 h-6 text-yellow-600" />
            Amount
          </label>
          <Input
            type="number"
            placeholder="Enter amount"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            className="h-14 text-lg mb-4"
          />
          <div className="grid grid-cols-3 gap-3">
            {amountOptions.map((amt) => (
              <Button
                key={amt}
                variant="outline"
                onClick={() => setAmount(amt.toString())}
                className="h-12 text-base font-semibold hover:bg-blue-50 hover:border-blue-500 transition-colors"
              >
                ₹{amt}
              </Button>
            ))}
          </div>
        </div>

        {/* Type Section */}
        <div className="bg-white rounded-lg shadow-md p-6 mb-6">
          <label className="flex items-center gap-2 text-lg font-bold mb-3">
            <Dices className="w-6 h-6 text-green-600" />
            Type
          </label>
          <Select value={type} onValueChange={setType}>
            <SelectTrigger className="h-14 text-lg">
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="Full">Full</SelectItem>
              <SelectItem value="Half">Half</SelectItem>
              <SelectItem value="Quick">Quick</SelectItem>
            </SelectContent>
          </Select>
        </div>

        {/* Game+ Section */}
        <div className="bg-white rounded-lg shadow-md p-6 mb-6">
          <label className="flex items-center gap-2 text-lg font-bold mb-3">
            <TrendingDown className="w-6 h-6 text-red-600" />
            Game+
          </label>
          <Input
            type="text"
            placeholder="Enter Game+"
            value={gamePlus}
            onChange={(e) => setGamePlus(e.target.value)}
            className="h-14 text-lg mb-4"
          />
          <div className="grid grid-cols-4 gap-3">
            {gamePlusOptions.map((gp) => (
              <Button
                key={gp}
                variant="outline"
                onClick={() => setGamePlus(gp)}
                className="h-12 text-base font-semibold hover:bg-red-50 hover:border-red-500 transition-colors"
              >
                {gp}
              </Button>
            ))}
          </div>
        </div>

        {/* Options Section */}
        <div className="bg-white rounded-lg shadow-md p-6 mb-6">
          <label className="flex items-center gap-2 text-lg font-bold mb-4">
            <Settings2 className="w-6 h-6 text-blue-600" />
            Options
          </label>
          <div className="space-y-4">
            <div className="flex items-center gap-3">
              <Checkbox
                id="freshId"
                checked={options.freshId}
                onCheckedChange={() => handleOptionChange('freshId')}
                className="w-6 h-6"
              />
              <label htmlFor="freshId" className="text-lg font-semibold cursor-pointer">
                Fresh Id
              </label>
            </div>
            <div className="flex items-center gap-3">
              <Checkbox
                id="codeAapDoge"
                checked={options.codeAapDoge}
                onCheckedChange={() => handleOptionChange('codeAapDoge')}
                className="w-6 h-6"
              />
              <label htmlFor="codeAapDoge" className="text-lg font-semibold cursor-pointer">
                Code aap doge
              </label>
            </div>
            <div className="flex items-center gap-3">
              <Checkbox
                id="noIPhone"
                checked={options.noIPhone}
                onCheckedChange={() => handleOptionChange('noIPhone')}
                className="w-6 h-6"
              />
              <label htmlFor="noIPhone" className="text-lg font-semibold cursor-pointer">
                No iPhone
              </label>
            </div>
            <div className="flex items-center gap-3">
              <Checkbox
                id="noKingPass"
                checked={options.noKingPass}
                onCheckedChange={() => handleOptionChange('noKingPass')}
                className="w-6 h-6"
              />
              <label htmlFor="noKingPass" className="text-lg font-semibold cursor-pointer">
                No king pass
              </label>
            </div>
            <div className="flex items-center gap-3">
              <Checkbox
                id="autoLoss"
                checked={options.autoLoss}
                onCheckedChange={() => handleOptionChange('autoLoss')}
                className="w-6 h-6"
              />
              <label htmlFor="autoLoss" className="text-lg font-semibold cursor-pointer">
                Auto loss
              </label>
            </div>
          </div>
        </div>

        {/* Agreement */}
        <div className="bg-white rounded-lg shadow-md p-4 mb-6">
          <p className="text-base">
            I am agree with the{' '}
            <a href="#" className="text-cyan-500 font-semibold hover:underline">
              Game Rules
            </a>
          </p>
        </div>

        {/* Send Table Button */}
        <Button
          onClick={handleSubmit}
          disabled={loading}
          className="w-full h-16 text-xl font-bold bg-gradient-to-r from-teal-700 to-teal-800 hover:from-teal-800 hover:to-teal-900 text-white shadow-lg rounded-xl transition-all transform hover:scale-[1.02]"
        >
          <Check className="w-6 h-6 mr-2" />
          {loading ? 'Sending...' : 'Send Table'}
        </Button>
      </div>
    </div>
  );
};

export default TableBooking;